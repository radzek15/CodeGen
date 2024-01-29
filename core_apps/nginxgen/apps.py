from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _lazy


class NginxgenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.nginxgen'
    verbose_name = _lazy('nginx_generator')
