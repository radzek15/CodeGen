from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/auth/', include('core_apps.users.urls')),
    path('api/dockerfile/', include('core_apps.dockerfilegen.urls')),
    path('api/dockercompose/', include('core_apps.dockercomposegen.urls')),
    path('api/nginx/', include('core_apps.nginxgen.urls')),
]
