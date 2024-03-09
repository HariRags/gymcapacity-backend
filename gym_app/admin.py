from django.contrib import admin
from .models import UserProfile
from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model


class YourModelAdmin(admin.ModelAdmin):       
  def has_delete_permission(self, request, obj=None):
    return False                         #removing the ability to delete users via the admin page
  def has_change_permission(self, request, obj=None):
        return False
  def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("<int:pk>/exit/", self.admin_site.admin_view(self.deny_view)),
        ]
        return my_urls + urls
  def deny_view(self, request, pk):
    user = get_user_model()
    mymembers =user.objects.get(pk=pk)     
    template = loader.get_template('delete.html')
    context = {
                  'mymembers': mymembers,
                 }
    if request.method == 'POST':    #get password
        password = request.POST.get('password')
        User = authenticate(username=mymembers.username, password=password)   #check if the password matches
        if User is not None:
            # Password is correct, delete the user
            User.delete()
            return redirect("admin:sr_app_gym_app_changelist")

        else:                    #if it doesnt match then redirect to the list
            return redirect("admin:sr_app_gym_app_changelist")
    return HttpResponse(template.render(context, request))
      
        
        



 
admin.site.register(UserProfile, YourModelAdmin)

# Register your models here.
