from django.urls import path, include
from rest_framework import routers
from api2.views import UserViewSet


router = routers.DefaultRouter()  # DefaultRouter 를 사용해
router.register(r'users', UserViewSet)  # users url - UserViewSet 매핑

urlpatterns=[
    path('', include(router.urls)),  # localhost:8000/api2/users 요청 시 UserViewSet.as_view() 호출됨
]