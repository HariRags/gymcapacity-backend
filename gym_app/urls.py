# gym_app/urls.py
from django.urls import path
from .views import (
    register, user_login, welcome,
    login_view, register_view, welcome_view, logout_view,exit_view,deletes,home_view,feedback,success
)

urlpatterns = [
    path('register/', register, name='register_api'),
    path('login/', user_login, name='login_api'),
    path('welcome/', welcome, name='welcome_api'),
    path('login-page/', login_view, name='login'),
    path('register-page/', register_view, name='register'),
    path('welcome-page/', welcome_view, name='welcome'),
    path('logout/', logout_view, name='logout'),
    path('welcome-page/exit/',exit_view, name='exit'),
    path('welcome-page/exit/delete/<int:id>',deletes, name='delete'),
    path('home/',home_view, name='home'),
    path('feedback/', feedback, name='feedback'),  #taking feedback from the user and creating a database table
     path('success/<int:feedback_id>/', success, name='success'),  #takes the data and shows in html template
]
