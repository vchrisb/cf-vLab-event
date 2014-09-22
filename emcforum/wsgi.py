"""
WSGI config for emcforum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
from dj_static import Cling
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emcforum.settings")

from django.core.wsgi import get_wsgi_application
application = Cling(get_wsgi_application())
