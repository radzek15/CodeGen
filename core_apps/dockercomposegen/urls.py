from django.urls import path

from .views import DockerComposeListCreateView, DockerComposeRetrieveUpdateDestroyView

urlpatterns = [
    path('instruction/', DockerComposeListCreateView.as_view(), name='compose-list-create'),
    path('instruction/<int:id>/',
         DockerComposeRetrieveUpdateDestroyView.as_view(),
         name='compose-retrieve-update-destroy'),
]
