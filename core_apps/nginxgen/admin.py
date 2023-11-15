from django.contrib import admin

from .models import NginxConfiguration, NginxInstruction


class NginxInstructionAdmin(admin.ModelAdmin):
    list_display = ['instruction', 'argument']
    list_display_links = ['instruction', 'argument']
    list_filter = ['instruction']
    ordering = ['instruction']


class NginxConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    list_display_links = ['name', 'value']
    list_filter = ['name']
    ordering = ['name']


admin.site.register(NginxInstruction, NginxInstructionAdmin)
admin.site.register(NginxConfiguration, NginxConfigurationAdmin)
