from rest_framework import generics, permissions
from my_api.permissions import IsOwnerOrReadOnly
from saved.models import Saved
from saved.serializers import SavedSerializer


class SavedList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavedSerializer
    queryset = Saved.objects.all()

    
