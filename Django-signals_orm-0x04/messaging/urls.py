from django.urls import path
from . import views

urlpatterns = [
    path("send/", views.send_message, name="send_message"),
    path("edit/<int:message_id>/", views.edit_message, name="edit_message"),
    path("history/<int:message_id>/", views.message_history, name="message_history"),
    path("delete-account/", views.delete_user, name="delete_user"),
]
