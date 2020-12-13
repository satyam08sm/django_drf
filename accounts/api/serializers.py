from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'uri']

    def get_uri(self, obj):
        return '/user/{id}/'.format(id=obj.id)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
        ]
        # extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        pw1 = data.get('password')
        pw2 = data.get('password2')
        if pw1 != pw2:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        # user = super().create(validated_data)
        # validated_data.pop('password2')
        user_obj = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user_obj.set_password(validated_data.get('password'))
        # user_obj.is_active = False
        user_obj.save()
        return user_obj

    # def validate(self, attrs):
    #     data = super().validate(attrs)
    #     refresh = RefreshToken.for_user(self.user)
    #     data['name'] = self.user.username
    #     data['refresh'] = str(refresh)
    #     data['access'] = str(refresh.access_token)
    #     return data

    def get_token(self, obj):
        refresh = RefreshToken.for_user(User)
        # request = self.context['request']
        # print(dir(request))
        # return request.user.is_authenticated
        return str(refresh.access_token)
