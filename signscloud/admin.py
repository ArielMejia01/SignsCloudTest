from django.contrib import admin
from . models import Stores, Brands, Deals
# Register your models here.

admin.site.register(Stores)
admin.site.register(Brands)
admin.site.register(Deals)