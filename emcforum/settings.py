"""
Django settings for emcforum project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']
else:
    SECRET_KEY = '&9cj-t8j*i5a7^y9@d^$at#g0!j_h=h++5stj=nb7z8u#l_y#&'

# SECURITY WARNING: don't run with debug turned on in production!
if 'DEBUG' in os.environ:
    if os.environ['DEBUG'] == 'True':
        DEBUG = True
    else:
        DEBUG = False
else:
    DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vLab',
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

ROOT_URLCONF = 'emcforum.urls'

WSGI_APPLICATION = 'emcforum.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
import json
mysql_srv = None
if 'VCAP_SERVICES' in os.environ:
    import json
    vcap_services = json.loads(os.environ['VCAP_SERVICES'])
    if 'cleardb' in vcap_services:
        mysql_srv = vcap_services['cleardb'][0]

if bool(mysql_srv):
    cred = mysql_srv['credentials']
    DATABASES = {
        'default': {
            'ENGINE': 'mysql.connector.django',
            'NAME': cred['name'],
            'USER': cred['username'],
            'PASSWORD': cred['password'],
            'HOST': cred['hostname'],
            'PORT': cred['port'],
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
            }
        }

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
