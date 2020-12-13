from django.urls import path
from .views import UserDetailAPIView, UserStatusListAPIView

urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view()),
    path('<str:username>/status/', UserStatusListAPIView.as_view()),
]
