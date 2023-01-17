from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    # path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
]

# /v1/posts/
# /v1/posts/{id}/

# /v1/posts/{post_id}/comments/
# /v1/posts/{post_id}/comments/{id}/

# /v1/groups/
# /v1/groups/{id}/

# /v1/follow/

# /v1/jwt/create/
# /v1/jwt/refresh/
# /v1/jwt/verify/
