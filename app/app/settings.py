"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6gut6+%i3)@p=#($9+uveea2jrifzp7eqkh5hp)=_pp@j4ewup'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
]

# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'discord.apps.DiscordConfig',

    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    "corsheaders",
    'django_crontab',


    'products',
    'base',
    'shop',
    'checkout',
    'order'
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    'https://discord.com',
    'http://localhost:8000',
    "https://www.mercadopago.com.br",
    "https://api.mercadopago.com"   # Adicione o domínio do seu frontend React aqui
    # Outros domínios permitidos, se houver
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware", # middleware for cors-headers
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'checkout.middleware.disable_csrf_for_notification',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'discord.middleware.AuthenticationExpirationMiddleware',
]



# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'corsheaders.middleware.CorsMiddleware',

#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'social_django.middleware.SocialAuthExceptionMiddleware',
# ]




CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'app.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DRF_ACCESS_POLICY = {"reusable_conditions": ["core.global_access_conditions"]}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_EXPOSE_HEADERS = ['Access-Control-Allow-Origin']

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Sao_Paulo'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'discord.DiscordUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'core.pagination.CustomPagination',
    # 'PAGE_SIZE': 100
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'access-token',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh-token',
    'JWT_AUTH_HTTPONLY':False,
    "JWT_TOKEN_CLAIMS_SERIALIZER": "app.jwt_serializer.CustomTokenObtainPairSerializer",
    # 'JWT_SERIALIZER_WITH_EXPIRATION': "app.jwt_serializer.CustomJWTSerializer",
    'JWT_AUTH_RETURN_EXPIRATION': True

}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',), 
    'USER_ID_FIELD': 'uuid',
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=3600),
    'REFRESH_TOKEN_LIFETIME': timedelta(seconds=3600),
    "ROTATE_REFRESH_TOKENS": True

}

JWT_AUTH_COOKIE_USE_CSRF = True

AUTHENTICATION_BACKENDS = [
    'discord.auth.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend'
]



LOGIN_URL = 'http://localhost:8000/auth/login'
# LOGIN_REDIRECT_URL = 'http://localhost:8000/api/user'
# LOGOUT_REDIRECT_URL = 'home'


CRONJOBS = [
    ('* * * * * */10', 'app.cron.payment_status_check_job')  # Substitua 'nomedoprojeto' pelo nome do seu projeto Django
]