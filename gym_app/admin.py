from django.contrib import admin
from .models import UserProfile, Feedback,User

# Register UserProfile model with admin site
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp')
    search_fields = ('user__username',)
    list_filter = ('timestamp',)

# Register Feedback model with admin site
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'feedback_type', 'timestamp')
    search_fields = ('name', 'roll')
    list_filter = ('feedback_type', 'timestamp')

# Register User model with admin site
admin.site.unregister(User)  # Unregister the default User model
admin.site.register(User)  # Register the default User model 
