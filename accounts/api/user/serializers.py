from rest_framework import serializers
from django.contrib.auth import get_user_model
from status.serializers import StatusSerializer, StatusInlineSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'uri', 'status']

    def get_uri(self, obj):
        return "/acc/api/user/{username}".format(username=obj.username)

    def get_status(self, obj):
        request = self.context.get('request')
        limit = 10
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass

        qs = obj.status_set.all().order_by("-timestamp")  # status_set = Status.objects.filter(user=obj)
        # print(type(StatusSerializer(qs, many=True).data))
        data = {
            'uri': self.get_uri(obj) + '/status/',
            'last': StatusInlineSerializer(qs.first()).data,
            'other': StatusInlineSerializer(qs[1:], many=True).data,
            'all': StatusInlineSerializer(qs, many=True).data,
            'recent': StatusInlineSerializer(qs[:limit], many=True).data,
        }

        return data
