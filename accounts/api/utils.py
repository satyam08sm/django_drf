from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework_simplejwt.tokens import RefreshToken


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken.for_user(self.user)
        data['name'] = self.user.username
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        print(refresh.payload)

        return data

    # def get_tokens_for_user(self, user):
    #     refresh = RefreshToken.for_user(user)
    #
    #     return {
    #         'refresh': "abc",
    #         'access': "xyz",
    #     }


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
