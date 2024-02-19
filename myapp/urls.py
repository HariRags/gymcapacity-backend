# myapp/urls.py
from django.urls import path
from myapp import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('userapi/', views.userapilogin ),
    path('userlist/',views.userlist),
    path('login/', views.student_login),
    path('list/', views.student_list)
]
