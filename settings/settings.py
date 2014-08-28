"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from config import *
SETTINGS_PATH = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6q6t77q!s@ens6c&3wbpr$895csf)i$bvnx&f8-a(n@@u!b**&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
    SETTINGS_PATH + '/templates/'
)

ALLOWED_HOSTS = []


# Application definition


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'jinja2',
    'south',
    'series',
    'home',
    'auth',
    'subtitles',
    'coffin',
    'storages'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'settings.context_processors.series_list',
)

ROOT_URLCONF = 'settings.urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'UTC'


USE_L10N = True

USE_TZ = True

USE_I18N = True
LANGUAGE_CODE = 'ru'
_ = lambda s: s
LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/upload/'
STATIC_ROOT = BASE_DIR + '/static/'
MEDIA_ROOT = BASE_DIR + '/static/upload/'

STATICFILES_DIRS = (
    SETTINGS_PATH + '/static/',
)

AUTH_USER_MODEL = 'auth.User'

JINJA2_EXTENSIONS = (
    'jinja2.ext.i18n',
)

LOGIN_URL = '/login/'

from settings_local import *


if not DEBUG:
    DEFAULT_FILE_STORAGE = 'settings.s3utils.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'settings.s3utils.StaticRootS3BotoStorage'
    AWS_STORAGE_BUCKET_NAME = 'eiscalle'
    S3_URL = 'http://%s.s3-website-eu-west-1.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL
    AWS_ACCESS_KEY_ID = 'AKIAIOORR2YSI7ASEK2A'
    AWS_SECRET_ACCESS_KEY = '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'