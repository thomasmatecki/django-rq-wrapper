# -*- coding: utf-8 -*-

# KISS
import os

ROOT_URLCONF = 'django_rq.tests.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REDIS_HOST = os.environ.get("REDIS_HOST", 'localhost')

SECRET_KEY = 'not-secret'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django_rq_wrapper',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

RQ_QUEUES = {
    'default': {
        'HOST': REDIS_HOST,
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': 500
    }
}

RQ = {
    'AUTOCOMMIT': False,
}


