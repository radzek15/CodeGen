from django.urls import path

from .views import DockerListCreateView, DockerRetrieveUpdateDestroyView

urlpatterns = [
    path('command/', DockerListCreateView.as_view(), name='docker-lc'),
    path('command/<int:id>/', DockerRetrieveUpdateDestroyView.as_view(), name='docker-rud'),
]
