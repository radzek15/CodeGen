from django.contrib import admin

from .models import DockerCommand


class DockerCommandAdmin(admin.ModelAdmin):
    list_display = ['instruction', 'argument', 'variable']
    list_display_links = ['instruction', 'argument', 'variable']
    list_filter = ['instruction']
    ordering = ['instruction']


admin.site.register(DockerCommand, DockerCommandAdmin)
