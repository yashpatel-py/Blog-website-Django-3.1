# this file is not auto genereted with django, it is created manually
# this file is connected with main project urls.py

from django.urls import path # this is the function which will handle all our urls and this will also b connectrd with views.py
from blog import views

urlpatterns = [
    path('', views.blogHome, name="blogHome"),
    path('search', views.search, name="search"),
    path('<str:slug>', views.blogPost, name="blogPost"),
]
