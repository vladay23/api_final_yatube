from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router_v1.register('follow', FollowViewSet, basename='follows')

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Документация API для проекта",
        contact=openapi.Contact(email="your.email@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('v1/jwt/create/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
