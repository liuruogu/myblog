__author__ = 'liu'
from django.conf.urls import url
from . import views

urlpatterns = [
    #^$ to the default page
    url(r'^$', views.index, name='index'),
]
