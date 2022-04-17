from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):  # api 가 내보낼 사항 지정
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']