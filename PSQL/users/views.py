from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import User
import json

# Get


def GetUsers(request):
    if request.method == "GET":
        # Fetch all users from the database
        all_users = User.objects.all()

        # Prepare a list of user data to return
        user_data = [{"id": user.id, "username": user.username} for user in all_users]

        # Prepare the response data
        data = {
            "users": user_data,
            "total_users": all_users.count()  # Include the total count of users
        }

        # Return a JsonResponse with the data
        return JsonResponse(data, status=200)
    
    # If the request method is not GET, return an error response
    return JsonResponse({"error": "Only GET method is allowed"}, status=405)


# Post

@csrf_exempt
def CreateUser(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse the request body
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return JsonResponse({"error": "Missing fields"}, status=400)

            # Check if Username Taken

            all_users = User.objects.all()

            # Create a new user
            user = User.objects.create(
                username=username, password=password)

            return JsonResponse({
                "message": "User created successfully",
                "user": {
                    "id": user.id,
                    "username": user.username,
                }
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)
