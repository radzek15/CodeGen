from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _lazy


class DockerfilegenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.dockerfilegen'
    verbose_name = _lazy('Dockerfile_generator')
