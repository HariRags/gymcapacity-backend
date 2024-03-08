from django.contrib import admin
from .models import UserProfile
from django.shortcuts import render, redirect

class YourModelAdmin(admin.ModelAdmin):
  def has_delete_permission(self, request, obj=None):
    return False


admin.site.register(UserProfile, YourModelAdmin)

# Register your models here.
