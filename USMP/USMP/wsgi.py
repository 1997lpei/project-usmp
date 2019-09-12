"""
WSGI config for USMP project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import sys

sys.path.append(r'/usr/local/apache2/htdocs/USMP/')

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "USMP.settings")
os.environ.setdefault("PYTHON_EGG_CACHE","/usr/local/.python-eggs")

application = get_wsgi_application()
