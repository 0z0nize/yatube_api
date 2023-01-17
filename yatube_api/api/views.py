from posts.models import Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# TODO:  Напишите свой вариант
# GET —
# возвращает все подписки пользователя, сделавшего запрос.
# Возможен поиск по подпискам по параметру search
# POST
# — подписать пользователя, сделавшего запрос на пользователя,
# переданного в теле запроса.
# При попытке подписаться на самого себя,
# пользователь должен получить информативное сообщение об ошибке.
# Проверка должна осуществляться на уровне API.
# Анонимный пользователь на запросы к этому эндпоинту
# должен получать ответ с кодом 401 Unauthorized.
# Сейчас ни самой модели Follow,
# ни обработчиков запросов в коде нет. Надо их написать.

# Применяйте вьюсеты.
# Для аутентификации используйте JWT-токены.
# У неаутентифицированных пользователей
# доступ к API должен быть только на чтение.
# Исключение — эндпоинт /follow/:
# доступ к нему должен предоставляться только
# аутентифицированным пользователям.
# Аутентифицированным пользователям разрешено
# изменение и удаление своего контента;
# в остальных случаях доступ предоставляется только для чтения.
# Добавление новых пользователей через API не требуется.

# Для проверки прав в DRF удобно использовать пермишены.
# При необходимости пишите и применяйте собственные классы разрешений.
# При описании вьюсетов для некоторых моделей имеет смысл
# наследоваться от собственного базового вьюсета.
# Не пренебрегайте этой возможностью.
# Работу с JWT-токенами удобно организовать при помощи библиотеки Djoser,
# но выбор решения за вами.
