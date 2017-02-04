"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
WSGI_DIR = os.path.dirname(BASE_DIR)
REPO_DIR = os.path.dirname(WSGI_DIR)

ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True
if ON_OPENSHIFT:
    DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', BASE_DIR)
else:
    DATA_DIR = DJ_PROJECT_DIR

import sys
sys.path.append(os.path.join(REPO_DIR, 'libs'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "boiaHFUVAEIOTR3BevoR"
OAUTH_REDIR = 'http://localhost:8000/scoutingapp/oauth2callback'
# SECURITY WARNING: don't run with debug turned on in production!
if ON_OPENSHIFT:
    DEBUG = os.environ.get('DEBUG') == 'True'
    OAUTH_REDIR = 'http://scouter-team179.rhcloud.com/scoutingapp/oauth2callback'
else:
    DEBUG = True
GOOGLE_OAUTH2_CLIENT_SECRETS_JSON=BASE_DIR+'/scoutingapp/client_secrets.json'
AUTH_USER_MODEL = 'scoutingapp.MyUser'

if ON_OPENSHIFT:
    from socket import gethostname
    ALLOWED_HOSTS = [
        # For internal OpenShift load balancer security purposes.
        gethostname(),
        # Dynamically map to the OpenShift gear name.
        os.environ.get('OPENSHIFT_APP_DNS'),
        #'example.com', # First DNS alias (set up in the app)
        #'www.example.com', # Second DNS alias (set up in the app)
    ]
else:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'scoutingapp',
    'django_tables2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

# GETTING-STARTED: change 'myproject' to your project name:
ROOT_URLCONF = 'scouter.urls'

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
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'scouter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # GETTING-STARTED: change 'db.sqlite3' to your sqlite3 database:
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    }
}
print(os.path.join(DATA_DIR, 'db.sqlite3'))
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(WSGI_DIR, 'static')
