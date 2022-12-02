from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-oll2*=&9pzaei2=7)o0g^%x(y221xe-8ox9!h6d!jn!rvyx95a"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INSTALLED_APPS += [
    "django_extensions",
    "debug_toolbar",
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]