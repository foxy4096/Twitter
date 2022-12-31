from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserProfile, get_user_model

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    fields = ['avatar',]
    verbose_name_plural = 'userprofile'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)