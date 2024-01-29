from rest_framework import serializers

from .models import DockerCommand


class DockerCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = DockerCommand
        fields = ['id', 'instruction', 'argument', 'variable']
