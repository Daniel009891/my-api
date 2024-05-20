from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from my_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        downvotes_count=Count('downvotes', distinct=True),
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        saved_count=Count('saved', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'saved__owner__profile',

    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'downvotes_count',
        'likes_count',
        'comments_count',
        'likes__created_at',
        'saved_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        downvotes_count=Count('downvotes', distinct=True),
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        saved_count=Count('saved', distinct=True),

    ).order_by('-created_at')
