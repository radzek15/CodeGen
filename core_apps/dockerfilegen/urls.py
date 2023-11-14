from django.urls import path

from .views import DockerListCreateView, DockerRetrieveUpdateDestroyView

urlpatterns = [
    path('command/', DockerListCreateView.as_view(), name='docker-list-create'),
    path('command/<int:id>/', DockerRetrieveUpdateDestroyView.as_view(), name='docker-retrieve-update-destroy'),
]
