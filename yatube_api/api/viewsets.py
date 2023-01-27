from rest_framework import mixins, viewsets

from .permissions import IsAuthOrReadOnly


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass


class IsAuthOrReadOnlyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthOrReadOnly]
