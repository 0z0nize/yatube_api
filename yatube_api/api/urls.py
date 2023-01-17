from django.urls import include, path

urlpatterns = [
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
