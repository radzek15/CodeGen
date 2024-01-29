from rest_framework import generics

from core_apps.dockerfilegen.permissions import IsSuperUserOrReadOnly

from .models import NginxConfiguration, NginxInstruction
from .serializers import NginxConfigurationSerializer, NginxInstructionSerializer


class NginxInstuctionListCreateView(generics.ListCreateAPIView):
    queryset = NginxInstruction.objects.all()
    serializer_class = NginxInstructionSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class NginxInstructionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NginxInstruction.objects.all()
    serializer_class = NginxInstructionSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    lookup_field = 'id'


class NginxConfigurationListCreateView(generics.ListCreateAPIView):
    queryset = NginxConfiguration.objects.all()
    serializer_class = NginxConfigurationSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class NginxConfigurationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NginxConfiguration.objects.all()
    serializer_class = NginxConfigurationSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    lookup_field = 'id'
