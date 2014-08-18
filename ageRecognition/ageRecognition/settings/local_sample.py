"""
Django local settings for ageRecognition project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
FACEBOOK_APP_ID = ''

FACEBOOK_APP_SECRET = ''


DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '<name>',                 # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '<your user>',
        'PASSWORD': '<your password>',
        'HOST': '127.0.0.1', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',           # Set to empty string for default.
    }
}
