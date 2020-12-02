from django.urls import path
from .views import StatusAPIView, StatusAPIDetailView

urlpatterns = [
    path('', StatusAPIView.as_view()),
    # path('create/', StatusCreateView.as_view()),
    path('<int:pk>/', StatusAPIDetailView.as_view()),
    # path('update/<int:pk>/', StatusUpdateView.as_view()),
    # path('delete/<int:pk>/', StatusDeleteView.as_view()),

]
