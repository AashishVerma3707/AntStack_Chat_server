from django.urls import path, include
from . import views
app_name = "chat_app"

urlpatterns = [
    path("", views.home),
    path("user_input/", views.user_check, name="user_input"),
    path("send", views.send, name="send_message")
]