"""
Django settings for ageRecognition project.
    
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/
    
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from configurations import importer
if not importer.installed:
    importer.install()

from configurations import Settings
from configurations.utils import uppercase_attributes
import os, sys, pkgutil, subprocess
from os.path import abspath, basename, dirname, join, normpath

__version__ = 'N/A'
try:
    import ageRecognition.version
    __version__ = ageRecognition.version.__version__
except ImportError:
    pass


class Base(Settings):
    SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_APP_DIR = os.path.dirname(SETTINGS_DIR)
    PROJECT_DIR = os.path.dirname(PROJECT_APP_DIR)
    ROOT_DIR = os.path.dirname(PROJECT_DIR)
    PORT = '8000'
    DOMAIN_NAME='localhost'
    SERVER_NAME='localhost'
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    THUMBNAIL_DEBUG = DEBUG

    if 'CONFIG_SERVER_NAME' in os.environ:
        SERVER_NAME = os.environ.get('CONFIG_SERVER_NAME')
    if 'CONFIG_HTTP_PORT' in os.environ:
        PORT = os.environ.get('CONFIG_HTTP_PORT')

    MAINTENANCE_MODE=0
    if 'MAINTENANCE_MODE' in os.environ:
        MAINTENANCE_MODE = os.environ.get('MAINTENANCE_MODE')

    STARTUP_ENV = {
        'DJANGO_CONFIGURATION': os.environ['DJANGO_CONFIGURATION'],
        'DJANGO_SETTINGS_MODULE': os.environ['DJANGO_SETTINGS_MODULE'],
    }

    SSL_PORT = ''
    SSL_CERTIFICATE = ''
    SSL_CERTIFICATE_KEY = ''

    TEST_DATA_PATH = os.path.join(PROJECT_DIR,'test_data')
    TEST_RUNNER = 'ageRecognition.test_runner.AgeRecognitionbTestRunner'
    CONFIG_GEN_TEMPLATES_DIR = os.path.join(PROJECT_DIR,'config','templates')
    CONFIG_GEN_GENERATED_DIR = os.path.join(PROJECT_DIR,'config','generated')

    DJANGO_ROOT = dirname(dirname(abspath(__file__)))
    SITE_ROOT = dirname(DJANGO_ROOT)

    SOURCE_GIT_URL = 'https://github.com/xbaro/ageRecognition.git'
    VIRTUAL_ENV = os.environ.get('VIRTUAL_ENV',None)

    AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
    AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'

    AGE_RECOGNITION_VERSION = __version__

    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = []

    ADMINS = (
        # ('Your Name', 'your_email@example.com'),
    )

    MANAGERS = ADMINS

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = 'UTC'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'en-us'

    SITE_ID = 1
    AGE_RECOGNITION_SITE_DOMAIN = 'sunai.uoc.edu'
    AGE_RECOGNITION_SITE_NAME = 'Age Recognition'

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # Absolute filesystem path to the directory that will hold user-uploaded files.
    # Example: "/var/www/example.com/media/"
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://example.com/media/", "http://media.example.com/"
    MEDIA_URL = '/media/'

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/var/www/example.com/static/"
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

    # URL prefix for static files.
    # Example: "http://example.com/static/", "http://static.example.com/"
    STATIC_URL = '/static/'

    # Additional locations of static files
    STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.FileSystemFinder',
        #'django.contrib.staticfiles.finders.DefaultStorageFinder',
        'compressor.finders.CompressorFinder',
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = 'p^_q=lzciqz$2mrtvxob#=$e4o&fdc96p=07rii94#au@r-#vw'

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        #'django.template.loaders.eggs.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django_facebook.middleware.FacebookCanvasMiddleWare',
    )

    ROOT_URLCONF = 'ageRecognition.urls'

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = 'ageRecognition.wsgi.application'

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        os.path.join(PROJECT_DIR,'templates'),
    )

    TEMPLATE_CONTEXT_PROCESSORS = Settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'allauth.account.context_processors.account',
        'allauth.socialaccount.context_processors.socialaccount',
        'ageRecognition.context_processors.app_version_proc',
        'django.core.context_processors.request',
        'django_facebook.context_processors.facebook',

    )

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
        'guardian.backends.ObjectPermissionBackend',
        'django_facebook.auth_backends.FacebookBackend',
    )

    INSTALLED_APPS = (
        # Standard django apps
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',

        # Analytics app that works with many services - IRJ 2013.7.29
        'analytical',
        'rest_framework',

        # This is used to manage the HTML page hierarchy for the competition
        'mptt',

        # TODO: Document the need for these
        'django_config_gen',
        'compressor',
        'django_js_reverse',
        'guardian',

        # Storage API
        'storages',

        # Migration app
        'south',

        # Django Nose !!Important!! This needs to come after South.
        'django_nose',

        # AgeRecognition apps
        'apps.canvas',

        # Authentication app, enables social authentication
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'tinymce',
        # 'oauth2_provider',

        # Facebook connection
        'django_facebook',

        # Search
        'haystack',

        # Thumbnail generator
        'sorl.thumbnail'
    )

    OPTIONAL_APPS = []
    INTERNAL_IPS = []

    # OAUTH2_PROVIDER = {
    #    'OAUTH2_VALIDATOR_CLASS': 'apps.authenz.oauth.Validator',
    # }

    # Email Configuration
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = '--- replace with sendgrid_username ---'
    EMAIL_HOST_PASSWORD = '--- replace with sendgrid_password ---'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'info@ageRecognition.org'
    SERVER_EMAIL = 'info@ageRecognition.org'

    # Authentication configuration
    # LOGIN_REDIRECT_URL = '/my'
    ANONYMOUS_USER_ID = -1
    # ACCOUNT_AUTHENTICATION_METHOD='username_email'
    # # ACCOUNT_EMAIL_REQUIRED=True
    # ACCOUNT_USERNAME_REQUIRED=False
    # ACCOUNT_EMAIL_VERIFICATION='none'

    # Our versioning
    AGE_RECOGNITION_LAST_COMMIT = "https://github.com/xbaro/ageRecognition/commit/%s" % AGE_RECOGNITION_VERSION.split()[0]

    # Django Analytical configuration
    GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-39111866-1'

    # Compress Configuration
    COMPRESS_PRECOMPILERS = (
        ('text/less', 'lessc {infile} {outfile}'),
        ('text/typescript', 'tsc {infile} --out {outfile}'),
    )

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
    }

    #HAYSTACK_CONNECTIONS = {
    #    'default': {
    #        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
    #        'URL': 'http://127.0.0.1:8983/solr'
    #        # ...or for multicore...
    #        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    #    },
    #}

    HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        },
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(MEDIA_ROOT, 'cache'),
        }
    }


    BUNDLE_SERVICE_URL = ""

    # Currently the search bar is hidden using this flag
    SHOW_BETA_FEATURES = False

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s %(levelname)s %(message)s'
            },
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                'stream': sys.stdout
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'ageRecognition': {
                'handlers': ['console'],
                'level': 'INFO'
            },
            'apps': {
                'handlers': ['console'],
                'level': 'INFO'
            }
        }
    }

    @classmethod
    def pre_setup(cls):
        if hasattr(cls,'OPTIONAL_APPS'):
            for a in cls.OPTIONAL_APPS:
                try:
                    __import__(a)
                except ImportError as e:
                    print e
                else:
                    cls.INSTALLED_APPS += (a,)
        cls.STARTUP_ENV.update({ 'CONFIG_HTTP_PORT': cls.PORT,
                                 'CONFIG_SERVER_NAME': cls.SERVER_NAME })
        if cls.SERVER_NAME not in cls.ALLOWED_HOSTS:
            cls.ALLOWED_HOSTS.append(cls.SERVER_NAME)

    @classmethod
    def post_setup(cls):
        if not hasattr(cls,'PORT'):
            raise AttributeError("PORT environmenment variable required")
        if not hasattr(cls,'SERVER_NAME'):
            raise AttributeError("SERVER_NAME environment variable required")


class DevBase(Base):

    OPTIONAL_APPS = ('debug_toolbar','django_extensions',)
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG=True
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TEMPLATE_CONTEXT': True,
        'ENABLE_STACKTRACES' : True,
    }
    # Increase amount of logging output in Dev mode.
    for logger_name in ('ageRecognition', 'apps'):
        Base.LOGGING['loggers'][logger_name]['level'] = 'DEBUG'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': os.path.join(Base.PROJECT_DIR,'dev_db.sqlite'), # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }

    # Send e-mails to the console during development
    #EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
