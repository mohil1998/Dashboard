from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/dash$', consumers.ChatConsumer),
    re_path(r'ws/dash/viewDash$', consumers.dashConsumer),

]
