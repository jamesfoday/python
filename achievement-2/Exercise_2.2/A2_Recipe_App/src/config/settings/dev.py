from .base import *
import environ
import os

# Initialize environment variables
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Load secrets and config from .env
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = []

# Database configuration - default to SQLite in development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Third party apps to add
THIRD_PARTY_APP = []

# Extend INSTALLED_APPS from base
INSTALLED_APPS += THIRD_PARTY_APP
