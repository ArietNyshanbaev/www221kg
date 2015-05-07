"""
Django settings for www221kg project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qownpf*%!re4n8%pc9%=7l+kd@1zdhe7m$+k7n+fp6d_4yqoff'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
    os.path.join(BASE_DIR,'main','templates','main'),
    os.path.join(BASE_DIR,'reservation','templates','reservation'),
    os.path.join(BASE_DIR,'news','templates','news'),
    os.path.join(BASE_DIR,'pro_owner','templates','pro_owner'),
)

ALLOWED_HOSTS = ['221.kg', 'www.221.kg']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bet',
    'mathfilters',
    'main',
    'password_reset',
    'news',
    'reservation',
    'pro_owner'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'www221kg.urls'

WSGI_APPLICATION = 'www221kg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_django_221',
        'USER': 'root',
        'OPTIONS': { "init_command": "SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED"} 
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static-root/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
STATIC_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR,'static-root')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


#email settings

#for gmail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'www.221.kg@gmail.com'
EMAIL_HOST_PASSWORD = '221120701'
EMAIL_PORT = 587
