from rest_framework import serializers

from .models import DockerComposeInstruction


class DockerComposeInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DockerComposeInstruction
        fields = ['id', 'key', 'value']
