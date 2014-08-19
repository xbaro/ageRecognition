"""
WSGI config for ageRecognition project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import site

site.addsitedir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../venv/lib/python2.7/site-packages'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ageRecognition.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
