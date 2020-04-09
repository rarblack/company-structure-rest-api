from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fcm/create/device/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create-device'),
    path('users/', include('user.urls')),
    path('announcements/', include('announcement.urls')),
    path('notifications/', include('notification.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
