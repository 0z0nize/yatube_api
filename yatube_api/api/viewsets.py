from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsAuthorOrReadOnly


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass


class IsAuthOrReadOnlyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly]
