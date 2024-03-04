# gym_auth/urls.py
from django.urls import path
from .views import (
    register, user_login, welcome,
    login_view, register_view, welcome_view, logout_view
)

urlpatterns = [
    path('register/', register, name='register_api'),
    path('login/', user_login, name='login_api'),
    path('welcome/', welcome, name='welcome_api'),
    path('login-page/', login_view, name='login'),
    path('register-page/', register_view, name='register'),
    path('welcome-page/', welcome_view, name='welcome'),
    path('logout/', logout_view, name='logout'),
]
