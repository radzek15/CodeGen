from django.urls import path

from .views import (
    NginxConfigurationListCreateView,
    NginxConfigurationRetrieveUpdateDestroyView,
    NginxInstructionRetrieveUpdateDestroyView,
    NginxInstuctionListCreateView,
)

urlpatterns = [
    path('instruction/', NginxInstuctionListCreateView.as_view(), name='nginx-instruction-lc'),
    path('instruction/<int:id>', NginxInstructionRetrieveUpdateDestroyView.as_view(), name='nginx-instruction-rud'),
    path('conf/', NginxConfigurationListCreateView.as_view(), name='nginx-conf-lc'),
    path('conf/<int:id>', NginxConfigurationRetrieveUpdateDestroyView.as_view(), name='nginx-conf-rud'),
]
