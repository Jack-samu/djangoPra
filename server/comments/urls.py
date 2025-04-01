from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("comments/<int:id>", views.comment, name="comment"),
]