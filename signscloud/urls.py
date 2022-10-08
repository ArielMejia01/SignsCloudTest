import imp
from django.conf.urls import url
from signscloud import views
from django.urls import path
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.storeApi, name='store'),
    #url(r'^store$', views.storeApi),
    #url(r'^store/([0-9]+)$', views.storeApi)
    path('store', views.storeApi, name='store'),
    path('brand', views.brandApi, name='brand'),
    #path('save', views.SaveFile, name='save'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)