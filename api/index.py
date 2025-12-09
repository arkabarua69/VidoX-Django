# api/index.py
import os
import sys

# প্রোজেক্ট রুট যদি ভিন্ন থাকে তাহলে ঠিক করে দাও (PROJECT_ROOT হলো manage.py থাকা ডিরেক্টরি)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# তোমার settings module ঠিক আছে কি নিশ্চিত করো
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vidox_project.settings")

# WSGI অ্যাপ পাওয়া
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Vercel expects variable named `app` or `handler`
# Export `app` pointing to Django WSGI application
app = application
