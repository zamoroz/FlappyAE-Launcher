from .base import *


DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "flappy",
        "USER": "flappy",
        "PASSWORD": "12345",
        "HOST": "db_flappy",
        "PORT": "5432",
    }
}
