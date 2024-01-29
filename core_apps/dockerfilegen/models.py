from django.db import models
from django.utils.translation import gettext_lazy as _lazy


class DockerCommand(models.Model):
    instruction = models.CharField(verbose_name=_lazy('command instruction'))
    argument = models.CharField(verbose_name=_lazy('command argument'), blank=True)
    variable = models.TextField(verbose_name=_lazy('command variable'), blank=True)

    class Meta:
        verbose_name = "Docker Command"
        verbose_name_plural = "Docker Commands"
        ordering = ['instruction']
        unique_together = ['instruction', 'argument', 'variable']

    def __str__(self):
        return f'{self.instruction} {self.argument} {self.variable}'
