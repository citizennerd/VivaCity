import os

import dj_database_url

from .settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = {'default': {'ENGINE': 'django.contrib.gis.db.backends.postgis', 'TEST_MIRROR': None, 'NAME': 's2988', 'TEST_CHARSET': None, 'TIME_ZONE': 'UTC', 'TEST_COLLATION': None, 'OPTIONS': {}, 'HOST': '10.180.234.117', 'USER': 's2988', 'TEST_NAME': None, 'PASSWORD': '5FDF4C88EFE1E72C76427BADB32FBEEC8EDA83D969D9A57C0C8D7898D675DC9D', 'PORT': 5432}}

SITE_ID = 1 # set this to match your Sites setup

MEDIA_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "media")
STATIC_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "static")

MEDIA_URL = "/site_media/media/" # make sure this maps inside of site_media_url
STATIC_URL = "/static/" # make sure this maps inside of site_media_url
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

FILE_UPLOAD_PERMISSIONS = 0640

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "django.request": {
            "propagate": True,
        },
    }
}