from .base import *
import environ

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7yojs1s)93zw)2fkv!hl)6p=$5o@_ehj8iscg2u-l5j670x0r@'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_METRICS_INDENT_JSON = 4
WAGTAIL_METRICS_GOOGLE_API_KEY = env('WAGTAIL_METRICS_GOOGLE_API_KEY')
