from django.db import models
from django.utils.translation import gettext_lazy as _lazy


class NginxInstruction(models.Model):
    instruction = models.CharField(verbose_name=_lazy('nginx instruction'), max_length=50)
    argument = models.CharField(verbose_name=_lazy('nginx instruction argument'), max_length=100, blank=True)

    class Meta:
        verbose_name = "Nginx Instruction"
        verbose_name_plural = "Nginx Instructions"
        ordering = ['instruction']
        unique_together = ['instruction', 'argument']

    def __str__(self):
        return f'{self.instruction} {self.argument}'


class NginxConfiguration(models.Model):
    name = models.CharField(verbose_name=_lazy('conf name'))
    value = models.TextField(verbose_name=_lazy('conf value'))

    class Meta:
        verbose_name = "Nginx Configuration"
        verbose_name_plural = "Nginx Configurations"
        ordering = ['name']
        unique_together = ['name', 'value']

    def __str__(self):
        return self.name
