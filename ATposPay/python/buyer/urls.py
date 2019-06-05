from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url('^$', views.index),
    url(r'^buyers/', views.BuyerList),
    url(r'^buyercreate/$', csrf_exempt(views.BuyerCreate), name='buyerCreate'),
]