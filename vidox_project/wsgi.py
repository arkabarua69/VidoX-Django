"""
WSGI config for vidox_project project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vidox_project.settings")

application = get_wsgi_application()

# --- Vercel expects 'app' or 'handler' variable for Python serverless entry ---
# Make the same WSGI application available under names Vercel looks for:
app = application
handler = application
