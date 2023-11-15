from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _lazy


class DockercomposegenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.dockercomposegen'
    verbose_name = _lazy('dockercompose_generator')
