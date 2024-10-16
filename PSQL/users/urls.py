from django.urls import path
from . import views

urlpatterns = [
    path('allusers/',  views.GetUsers),
    path('create-user/',  views.CreateUser),
]
