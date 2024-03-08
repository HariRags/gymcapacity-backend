from django.contrib import admin
from .models import UserProfile
 
class YourModelAdmin(admin.ModelAdmin):       
  def has_delete_permission(self, request, obj=None):
    return False                         #removing the ability to delete users via the admin page
 

admin.site.register(UserProfile, YourModelAdmin)

# Register your models here.
