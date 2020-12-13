from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .serializers import RegisterSerializer
from accounts.api.user.serializers import UserDetailSerializer
from .permissions import AnonPermissionOnly, IsOwnerOrReadOnly
from status.serializers import StatusInlineSerializer
from status.models import Status

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}


class UserStatusListAPIView(generics.ListAPIView):
    serializer_class = StatusInlineSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username', None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)


class RegisterAPIView(generics.CreateAPIView):
    qs = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AnonPermissionOnly]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

# class AuthView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return Response({'detail': 'Already authenticated'}, status=400)
#         data = request.data
#         username = data['username']
#         password = data['password']
#         user = authenticate(username=username, password=password)
#         qs = User.objects.filter(
#             Q(username__iexact=username) or
#             Q(email__iexact=username)
#         ).distinct()
#         if qs.count() == 1:
#             user_obj = qs.first()
#             if user_obj.check_password(password):
#                 user = user_obj
#                 refresh = RefreshToken.for_user(user)
