import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bihar_b2b_tours.settings")
application = get_asgi_application()
