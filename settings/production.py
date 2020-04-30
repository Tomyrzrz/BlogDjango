from .base import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['appcomputadorastimo.herokuapp.com'] 


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd4i4pnqhdk2dl',
        'USER': 'znftiujsmneceo',
        'PASSWORD': '7f69a6f88735e4364c97cab593902a639e1bf69ce972231da3f0b7e2e17c4faf',
        'HOST': 'ec2-18-209-187-54.compute-1.amazonaws.com',
        'PORT': 5432
    }
}


