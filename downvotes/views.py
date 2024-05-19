from rest_framework import generics, permissions
from my_api.permissions import IsOwnerOrReadOnly
from downvotes.models import DownVote


class DownVoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]