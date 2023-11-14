from rest_framework import generics

from .models import DockerCommand
from .permissions import IsSuperUserOrReadOnly
from .serializers import DockerCommandSerializer


class DockerListCreateView(generics.ListCreateAPIView):
    serializer_class = DockerCommandSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = DockerCommand.objects.all()


class DockerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DockerCommand.objects.all()
    serializer_class = DockerCommandSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    lookup_field = 'id'
