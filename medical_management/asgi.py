"""
ASGI config for medical_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_management.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http' : get_asgi_application(),
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(routing.websocket_urlpatterns)
            )
        )
    })
