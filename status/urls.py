from django.urls import path
from .views import StatusAPIView

urlpatterns = [
    path('', StatusAPIView.as_view()),
    # path('create/', StatusCreateView.as_view()),
    # path('<int:pk>/', StatusDetailView.as_view()),
    # path('update/<int:pk>/', StatusUpdateView.as_view()),
    # path('delete/<int:pk>/', StatusDeleteView.as_view()),

]
