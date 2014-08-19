"""
WSGI config for ageRecognition project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import site
import os
import site
from django.core.wsgi import get_wsgi_application

# Provide the virtual environment path
venvdir = os.path.abspath(os.path.join(os.path.abspath(__file__),'../'))

site.addsitedir(os.path.join(venvdir,'venv/lib/python2.7/site-packages'))

# Provide the application settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ageRecognition.settings")

# Get the application
application = get_wsgi_application()
