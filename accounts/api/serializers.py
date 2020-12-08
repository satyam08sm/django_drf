from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
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
        user_obj.save()
        return user_obj
