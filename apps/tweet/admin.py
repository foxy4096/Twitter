from django.contrib import admin

from .models import *

class TweetAdmin(admin.ModelAdmin):
    list_display = ('body', 'created_at', 'user')
    fields = ('body', 'user')
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change):
        if obj.user is None:
            obj.user = request.user
        obj.save()
    
    def get_queryset(self, request):
        qs = super(TweetAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(Tweet, TweetAdmin)