from rest_framework import serializers

from .models import NginxConfiguration, NginxInstruction


class NginxInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NginxInstruction
        fields = ['id', 'instruction', 'argument']


class NginxConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NginxConfiguration
        fields = ['id', 'name', 'value']
