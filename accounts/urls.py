from django.urls import path, include
from accounts.api.views import RegisterAPIView

urlpatterns = [
    path('', RegisterAPIView.as_view())
]
