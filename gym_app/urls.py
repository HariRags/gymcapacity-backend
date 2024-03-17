from django.urls import path
from .views import register_view, list_view, delete_view, feedback_view,last_deleted_user_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('list/', list_view, name='list'),
    path('delete/<int:id>/', delete_view, name='delete'),
    path('feedback/', feedback_view, name='feedback'),
     path('last-deleted-user/', last_deleted_user_view, name='last_deleted_user')
]
