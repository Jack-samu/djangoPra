from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name='homepage'),
    path("turnback/", views.return_something, name='jsonpage'),
    path("turnaround/", views.turn_around, name='aaaaa'),
    path("sayhello;<str:name>/", views.sayhello, name="sayhello"),
    path("say/", views.echo),
    path("what/", views.whatever),
]