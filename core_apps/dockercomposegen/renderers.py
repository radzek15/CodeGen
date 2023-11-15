from rest_framework_yaml.renderers import YAMLRenderer

from .models import DockerComposeInstruction


class CustomYAMLRenderer(YAMLRenderer):
    media_type = 'text/yaml'
    format = 'yaml'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, DockerComposeInstruction):
            yaml_data = f"{data.key}: {data.value}"
            return yaml_data
        return super().render(data, accepted_media_type, renderer_context)
