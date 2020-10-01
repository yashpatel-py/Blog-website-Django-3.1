# this file is not auto genereted with django, it is created manually
# this file is connected with main project urls.py

from django.urls import path # this is the function which will handle all our urls and this will also b connectrd with views.py
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('materials', views.materials, name='materials'),
    path('buy_course', views.buy_course, name='buy_course'),
    path('counselling', views.counselling, name='counselling'),
    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
]
