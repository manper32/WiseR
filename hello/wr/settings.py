"""
Django settings for wr project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h@_xgq-ncvi+$f7i)lk0$24cx@&ngs$7f+u=)3(r*9oz-o-5kv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'testserver',
    'localhost',
    '10.150.1.77',
    'cbpodev.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'file_app',
    'Vicidial',
    'Email',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    'http://10.150.1.79:8001',
)

ROOT_URLCONF = 'wr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'wr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'public': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Bogota': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_bogota'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Maf': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_maf'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Cartera ok': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_carteraok'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Claro': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_claro'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Codensa': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_codensa'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Colpatria': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_colpatria'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Davivienda': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_davivienda'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Falabella': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_falabella'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Banco popular': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_popular'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Progresa': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_progresa'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Cartera propia': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_propia'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Qnt': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_qnt'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'Santander': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_santander'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
    'AVANTEL': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=cbpo_avantel'
        },
        'NAME': 'login',
        'USER' : 'bi',
        'PASSWORD' : 'juanitoMeToco2020',
        'HOST' : '10.150.1.77',
        'PORT' : '5432'
    },
}

DATABASE_ROUTERS = [
    'file_app.routers.file_appRouter',
    'file_app.routers.file_appRouter2',
    'file_app.routers.file_appRouter3',
    'file_app.routers.file_appRouter4',
    'file_app.routers.file_appRouter5',
    'file_app.routers.file_appRouter6',
    'file_app.routers.file_appRouter7',
    'file_app.routers.file_appRouter8',
    'file_app.routers.file_appRouter9',
    'file_app.routers.file_appRouter10',
    'file_app.routers.file_appRouter11',
    'file_app.routers.file_appRouter12',
    'file_app.routers.file_appRouter13',
]


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# # path to the directory where you would want to store the uploaded files
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static')
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_USER = 'analista.db@cobrando.com.co'
EMAIL_HOST_USER = 'carterarecuperacion@cobrando.com.co'
EMAIL_HOST_PASSWORD = 'Bogota*1234'