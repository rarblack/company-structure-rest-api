from django.urls import path
from .views import NotificationsListAPIView

app_name = 'notification'
urlpatterns = [
    path('users/<int:pk>', NotificationsListAPIView.as_view(), name='list-user-notifications')
]
