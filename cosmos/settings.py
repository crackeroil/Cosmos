"""
Django settings for cosmos project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys

import secret_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_settings.secrets["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = secret_settings.secrets["DEBUG"]

# TESTING: detect when in testing mode
# https://stackoverflow.com/questions/4088253/django-how-to-detect-test-environment-check-determine-if-tests-are-being-ru/7651002#7651002
TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"

# Pretix config
PRETIX_DOMAIN = secret_settings.secrets["PRETIX_DOMAIN"]
AUTHORIZATION_HEADER = secret_settings.secrets["PRETIX_AUTHORIZATION_HEADER"]

ALLOWED_HOSTS = secret_settings.secrets["ALLOWED_HOSTS"]

# Application definition


ROOT_URLCONF = "cosmos.urls"

WSGI_APPLICATION = "cosmos.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": secret_settings.secrets["DATABASES"]["DEFAULT"]["NAME"],
        "USER": secret_settings.secrets["DATABASES"]["DEFAULT"]["USER"],
        "PASSWORD": secret_settings.secrets["DATABASES"]["DEFAULT"]["PASSWORD"],
        "HOST": secret_settings.secrets["DATABASES"]["DEFAULT"]["HOST"],
        "PORT": secret_settings.secrets["DATABASES"]["DEFAULT"]["PORT"],
        "OPTIONS": secret_settings.secrets["DATABASES"]["DEFAULT"]["OPTIONS"],
    },
}

# Cache
# https://docs.djangoproject.com/en/3.0/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": secret_settings.secrets["CACHE"]["REDIS_URL"],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PARSER_CLASS": "redis.connection.HiredisParser",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "Europe/Amsterdam"

USE_I18N = False

# Use server-side locales
USE_L10N = False

# Reference: https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#date
# https://docs.djangoproject.com/en/3.2/ref/settings/#date-format
DATE_FORMAT = "d/m/Y"
# https://docs.djangoproject.com/en/3.2/ref/settings/#time-format
TIME_FORMAT = "H:i"
# https://docs.djangoproject.com/en/3.2/ref/settings/#datetime-format
DATETIME_FORMAT = "d/m/Y H:i"

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(DATA_DIR, "media")
STATIC_ROOT = os.path.join(DATA_DIR, "static")

STATICFILES_STORAGE = "pipeline.storage.PipelineManifestStorage"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.PipelineFinder",
]

PIPELINE = {
    "CSS_COMPRESSOR": "pipeline.compressors.yuglify.YuglifyCompressor",
    "YUGLIFY_BINARY": "node_modules/.bin/yuglify",
    "JS_COMPRESSOR": "pipeline.compressors.closure.ClosureCompressor",
    "CLOSURE_BINARY": "node_modules/.bin/google-closure-compiler",
    "STYLESHEETS": {
        "cosmos": {
            "source_filenames": {
                "cosmos/css/core.css",
                "cosmos/css/gmm.css",
                "cosmos/css/photos.css",
                "cosmos/css/news.css",
                "cosmos/css/about.css",
                "cosmos_events/css/events.css",
            },
            "output_filename": "cosmos/css/cosmos.css",
        },
        "cosmos_users": {
            "source_filenames": {"cosmos_users/css/auth.css"},
            "output_filename": "cosmos_users/css/cosmos_users.css",
        },
    },
    "JAVASCRIPT": {
        "cosmos": {
            "source_filenames": {
                "cosmos/js/gmm.js",
                "cosmos/js/photos.js",
                "cosmos/js/about.js",
                "cosmos_events/js/events.js",
            },
            "output_filename": "cosmos/js/cosmos.js",
        },
    },
}

SITE_ID = 1

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "cosmos", "templates")],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.csrf",
                "django.template.context_processors.tz",
                "django.template.context_processors.static",
            ],
            "loaders": ["django.template.loaders.filesystem.Loader", "django.template.loaders.app_directories.Loader"],
        },
    },
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "crum.CurrentRequestUserMiddleware",
]

INSTALLED_APPS = [
    "cosmos",
    "apps.core",
    "apps.users",
    "apps.events",
    "apps.async_requests",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "django_better_admin_arrayfield",
    "pipeline",
    "django_celery_results",
    "oauth2_provider",
    "corsheaders",
    "formtools",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_sendfile",
    "django_cleanup.apps.CleanupConfig",
    "ckeditor",
    "django_celery_beat",
]

LANGUAGES = (
    # Customize this
    ("en", "en"),
)

X_FRAME_OPTIONS = "SAMEORIGIN"

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

# Logging
# https://docs.djangoproject.com/en/3.1/topics/logging/
LOGGING_FOLDER = secret_settings.secrets["LOGGING"]["FOLDER"]  # relative to root of project
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        # copied from DEFAULT_LOGGING https://github.com/django/django/blob/master/django/utils/log.py
        "verbose": {"()": "django.utils.log.ServerFormatter", "format": "[{server_time}] {message}", "style": "{"}
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "filters": ["require_debug_true"], "formatter": "verbose"},
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "midnight",
            "interval": 1,
            "filename": os.path.join(LOGGING_FOLDER, "debug.log"),
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console", "mail_admins"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

# Email
# https://docs.djangoproject.com/en/3.1/topics/email/
# https://support.google.com/a/answer/2956491?hl=en
EMAIL_HOST = secret_settings.secrets["EMAIL"]["HOST"]
EMAIL_PORT = secret_settings.secrets["EMAIL"]["PORT"]
EMAIL_HOST_USER = secret_settings.secrets["EMAIL"]["USERNAME"]
EMAIL_HOST_PASSWORD = secret_settings.secrets["EMAIL"]["PASSWORD"]
EMAIL_USE_TLS = secret_settings.secrets["EMAIL"]["USE_TLS"]

DEFAULT_FROM_EMAIL = secret_settings.secrets["EMAIL_GSUITE"]["USERNAME"]

LOGIN_URL = "/accounts/login/"
LOGOUT_REDIRECT_URL = "/"

# Security
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

SECURE_REFERRER_POLICY = "same-origin"

# Celery
CELERY_BROKER_URL = secret_settings.secrets["CELERY"]["REDIS_URL"]
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_WORKER_HIJACK_ROOT_LOGGER = True
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

SENDGRID_WEBHOOK_SIGNATURE = secret_settings.secrets["SENDGRID_WEBHOOK_SIGNATURE"]

# Crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

if DEBUG:
    SENDFILE_BACKEND = "django_sendfile.backends.development"
else:
    SENDFILE_BACKEND = "django_sendfile.backends.nginx"
SENDFILE_ROOT = os.path.join(DATA_DIR, "media/")
SENDFILE_URL = "/protected-media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_CONFIGS = {
    "default": {"width": "100%"},
}
