import imp
from django.conf.urls import url
from signscloud import views
from django.urls import path

urlpatterns=[
    #url(r'^store$', views.storeApi),
    #url(r'^store/([0-9]+)$', views.storeApi)
    path('store', views.storeApi, name='store')
]