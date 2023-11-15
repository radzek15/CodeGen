from rest_framework import generics
from rest_framework_yaml.renderers import YAMLRenderer

from .models import DockerComposeInstruction
from .permissions import IsSuperUserOrReadOnly
from .renderers import CustomYAMLRenderer
from .serializers import DockerComposeInstructionSerializer


class DockerComposeListCreateView(generics.ListCreateAPIView):
    serializer_class = DockerComposeInstructionSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = DockerComposeInstruction.objects.all()
    renderer_classes = [CustomYAMLRenderer]


class DockerComposeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DockerComposeInstructionSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = DockerComposeInstruction.objects.all()
    lookup_field = 'id'
    renderer_classes = [CustomYAMLRenderer]
