from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_extensions'
]

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
TEST_OUTPUT_VERBOSE = 2
TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_FILE_NAME = 'test-report.xml'

LOGGING = {}
