from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='bloghome'),
    path('blog/<str:title>/', views.detail, name="get_post"),
]