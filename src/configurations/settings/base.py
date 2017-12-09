import os
from os.path import abspath
from os.path import dirname
from os.path import join

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

DEBUG = False
ALLOWED_HOSTS = []

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
)

LOCAL_APPS = (
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}

ROOT_URLCONF = 'configurations.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'configurations.wsgi.application'

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in STATICFILES_DIRS.
STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'static_cdn')

MEDIA_URL = '/media/'
MEDIA_ROOT = join(os.path.dirname(BASE_DIR), 'media_cdn')

STATICFILES_DIRS = [
    join(BASE_DIR, 'static'),
]


# $DJANGO_ENVIRONMENT is set in docker-compose yaml file
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT')
if ENVIRONMENT == 'production':
    from .production import *
elif ENVIRONMENT == 'staging':
    from .staging import *
elif ENVIRONMENT == 'test':
    from .test import *
else:
    from .dev import *
