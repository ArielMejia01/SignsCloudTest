from pyexpat import model
from django.db import models

# Create your models here.
# Modulos necesarios
class Stores(models.Model):
    storeId = models.AutoField(primary_key=True)
    brand = models.IntegerField(null=False, blank=False)
    identifier = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    
class Brands(models.Model):
    brandId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    #logo = models.URLField(max_length=200)
    logo = models.ImageField(upload_to='imagenes/', verbose_name='Imagen')

class Deals(models.Model):
    dealId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    store = models.IntegerField(null=False, blank=False)
    #image = models.URLField(max_length=200)
    image = models.ImageField(upload_to='imagenes/', verbose_name='Imagen')  
    price =   models.DecimalField(max_digits = 10, decimal_places=2)
