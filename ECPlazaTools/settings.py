"""
Django settings for ECPlaza Tools project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

import dj_database_url
import dotenv as env
import django_heroku
from django.contrib.admin import AdminSite

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env.load_dotenv(os.path.join(BASE_DIR, '.env'))
config = {
    'BASE_DIR': BASE_DIR,
    'DATE_FORMAT': os.getenv('DATE_FORMAT'),
    'GOOGLE_USER_ID': os.getenv('GOOGLE_USER_ID'),
    'LANGUAGE_CODE': os.getenv('LANGUAGE_CODE'),
    'SENDGRID_API_KEY': os.getenv('SENDGRID_API_KEY'),
    'SENDGRID_URL': os.getenv('SENDGRID_URL'),
    'TIME_ZONE': os.getenv('TIME_ZONE'),
    'TOUR_API_KEY': os.getenv('TOUR_API_KEY'),
    'SCOUT_KEY': os.getenv('SCOUT_KEY')
}

for key, value in config.items():
    os.environ[key] = value

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r5#9$04@$xnhm!@3op21hop4n@fsybo$o9ko-pb2jbhrre6gro'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'scout_apm.django',
    'accounts.apps.AccountsConfig',
    'file_app.apps.FileAppConfig',
    'api.apps.APIConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatterbot.ext.django_chatterbot',
    'corsheaders',
    'django_createuser',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken'
]
CORS_ORIGIN_ALLOW_ALL = True
INSTALLED_APPS += ['django_extensions']

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

ROOT_URLCONF = 'ECPlazaTools.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]
WSGI_APPLICATION = 'ECPlazaTools.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')),
}

AdminSite.login_template = os.path.join(TEMPLATES[0].get('DIRS')[0], 'accounts', 'login.html')

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/'

# CORS Settings

CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "https://ecplaza-tools.herokuapp.com",
    "http://localhost:8000",
    "http://127.0.0.1:9000"
]

# Scout Settings

SCOUT_MONITOR = True
SCOUT_KEY = os.environ.get('SCOUT_KEY')
SCOUT_NAME = 'A FRIENDLY NAME FOR YOUR APP'

# ChatterBot Settings

CHATTERBOT = {
    'name': 'Tech Support Bot',
    'django_app_name': 'django_chatterbot',

    'logic_adapters': ['chatterbot.logic.BestMatch'],
    'trainer': 'chatterbot.trainers.ChatterBotCorpusTrainer',
    'training_data': [
        'chatterbot.corpus.english.greeting',
        'chatterbot.corpus.english.conversations',
        # 'chatterbot.corpus.custom.myown',
        'chatterbot.corpus.korean.greeting',
        'chatterbot.corpus.korean.conversations',
    ],

    'storage_adapter': 'chatterbot.storage.SQLStorageAdapter',
    'database_uri': os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-us')

TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Upload Settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 3000000
UPLOADS_PATH = os.path.join(BASE_DIR, os.path.join('static', 'uploads'))
FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, os.path.join('static', 'tmp-uploads'))
FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'ECPlazaTools.handlers.CustomTempFileUploadHandler'
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
