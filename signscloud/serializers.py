from ast import Store
from dataclasses import fields
from rest_framework import serializers
from signscloud.models import Stores, Brands, Deals

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = ('storeId', 'brand', 'identifier', 'name', 'address')
    
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ('brandId', 'name', 'logo')

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = ('dealId', 'name', 'store', 'image', 'price')