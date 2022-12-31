from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.core.urls")),
    path('tweet/', include("apps.tweet.urls")),
    path('user/', include("apps.userprofile.urls")),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
            }),
            
]
