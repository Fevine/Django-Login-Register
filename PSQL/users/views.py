from django.shortcuts import render
from django.http import JsonResponse
from . import models

# Create your views here.


def GetUsers(request):
    all_users = models.User.objects.all()

    user_data = [{"id": user.id, "username": user.username}
                 for user in all_users]

    data = {
        "users": user_data
    }

    return JsonResponse(data)
