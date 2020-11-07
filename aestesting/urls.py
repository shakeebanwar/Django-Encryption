from django.contrib import admin
from django.urls import path , include
from aestesting.views import User_Signup,home

urlpatterns = [
  
    path('User_Signup',User_Signup.as_view()),
    path('',home.as_view()),
]