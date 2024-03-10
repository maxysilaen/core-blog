from rest_framework import (
    viewsets
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    Post,
)
from .permissions import (
    IsOwnerOrReadOnly)
from .serializers import (
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)