"""
Django settings for pokedex project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# ----------------------------------------------------------
# SECURITY
# ----------------------------------------------------------

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-development-only-key"
)

# True locally, False on Render
DEBUG = "RENDER" not in os.environ

# Local hosts
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# Render automatically provides this
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# ----------------------------------------------------------
# INSTALLED APPS
# ----------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]


# ----------------------------------------------------------
# MIDDLEWARE
# ----------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Static file serving in production
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ----------------------------------------------------------
# URL / WSGI
# ----------------------------------------------------------

ROOT_URLCONF = 'pokedex.urls'

WSGI_APPLICATION = 'pokedex.wsgi.application'


# ----------------------------------------------------------
# TEMPLATES
# ----------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ----------------------------------------------------------
# DATABASE
# ----------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ----------------------------------------------------------
# PASSWORD VALIDATION
# ----------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    },
]


# ----------------------------------------------------------
# INTERNATIONALIZATION
# ----------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ----------------------------------------------------------
# STATIC FILES
# ----------------------------------------------------------

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'core' / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

if not DEBUG:
    STATICFILES_STORAGE = (
        'whitenoise.storage.CompressedManifestStaticFilesStorage'
    )


# ----------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# ----------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'