from rest_framework import serializers
from .models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'user', 'content', 'image']

        read_only_fields = ['user']

    def validate_content(self, value):
        if len(value) > 10000:
            raise serializers.ValidationError("content is long")
        return value

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None

        image = data.get('image', None)

        if content is None and image is None:
            raise serializers.ValidationError("image or content is required")

        return data
