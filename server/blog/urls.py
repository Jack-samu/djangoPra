from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='bloghome'),
    path('blog/<str:title>/', views.detail, name="get_post"),
    path('search/', views.search, name='search'),
    path('intro/', views.intro, name='introduction'),
    path('archive/', views.archive, name='archive'),
]