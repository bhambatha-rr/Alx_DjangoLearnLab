from django.urls import path
from .views import NotificationListView, MarkNotificationsAsReadView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/mark-as-read/', MarkNotificationsAsReadView.as_view(), name='notification-mark-read'),
]
