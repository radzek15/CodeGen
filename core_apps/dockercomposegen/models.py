from django.db import models
from django.utils.translation import gettext_lazy as _lazy


class DockerComposeInstruction(models.Model):
    key = models.CharField(verbose_name=_lazy('Key'), max_length=50)
    value = models.TextField(verbose_name=_lazy('Value'))

    class Meta:
        verbose_name = "Docker Compose Instruction"
        verbose_name_plural = "Docker Compose Instructions"
        unique_together = ['key', 'value']

    def __str__(self):
        return f'{self.key}: {self.value}'
