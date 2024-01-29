from django.contrib import admin

from .models import DockerComposeInstruction


class DockerComposeInstructionAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    list_display_links = ['key', 'value']
    list_filter = ['key']


admin.site.register(DockerComposeInstruction, DockerComposeInstructionAdmin)
