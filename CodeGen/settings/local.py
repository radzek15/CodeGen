from .base import *  # noqa
from .base import env

CORS_ALLOW_ALL_ORIGINS = True

SECRET_KEY = env('DJANGO_SECRET_KEY', default='ltjkifBGrCFPluisH5Dfwu2qWxiUm7B9ZNPbA74YpEx_-rh4dSE',)

DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']
