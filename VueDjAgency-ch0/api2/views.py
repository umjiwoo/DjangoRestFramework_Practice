from django.contrib.auth.models import User
from rest_framework import viewsets
from api2.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):  # ViewSet -> 뷰가 할 행동 정의
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 간단한 코드에 의해 모델에 대한 CRUD 기능이 전부 구현됨 -> ModelViewSet 클래스를 상속받았기 때문
