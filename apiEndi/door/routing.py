from django.urls import re_path
from .consumers import Chat

websocket_urlpatterns = [
    re_path(r'chat', Chat.as_asgi()),
]
