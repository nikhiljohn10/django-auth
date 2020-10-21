from .default import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'accounts',
    'dashboard',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

AUTH_USER_MODEL = 'accounts.User'

LANGUAGE_CODE = 'en-in'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = False

STATIC_ROOT = BASE_DIR/'static'

MEDIA_URL = '/assets/'
MEDIA_ROOT = BASE_DIR.parent/'assets'

LOGIN_URL='/auth/login/'
LOGIN_REDIRECT_URL='/dashboard/'
LOGOUT_REDIRECT_URL='/auth/login/'

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 # One month
