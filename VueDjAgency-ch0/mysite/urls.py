# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
#
# from mysite.views import HomeView
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # shkim
#     path('', HomeView.as_view(), name='home'),
#     path('blog/', include('blog.urls')),
#     path('api/', include('api.urls')),
#     # DRF
#     path('api/auth/', include('rest_framework.urls')),
# ]
#
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include

# serialize.py 파일 (일반 장고 프로그램에는 x, drf 에만 있는 파일)로 이동
# class UserSerializer(serializers.HyperlinkedModelSerializer):  # api 가 내보낼 사항 지정
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# views.py 로 이동
# class UserViewSet(viewsets.ModelViewSet):  # ViewSet -> 뷰가 할 행동 정의
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# Router 관련 코드 하위 url 로 이동
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api2/', include('api2.urls')),

    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # -> login 버튼 보이도록 설정, 사용하고자 한다면 하위 urls.py 보다 root urls.py 에 지정 (; 하위 파일에 두면 작업할 내용 생김)
]
