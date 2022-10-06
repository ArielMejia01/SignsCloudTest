import imp
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

#Importar los modelos y las clases serializadoras
from signscloud.models import Stores, Brands, Deals
from signscloud.serializers import StoreSerializer, BrandSerializer, DealSerializer

# Create your views here.
# vamos a obtner todas las tiendas
@csrf_exempt
def storeApi(request, id=0):
    if request.method=='GET':
        store = Stores.objects.all()
        store_serializer = StoreSerializer(store, many=True)
        return JsonResponse(store_serializer.data, safe=False)
    elif request.method=='POST':
        store_data = JSONParser().parse(request)
        store_serializer = StoreSerializer(data=store_data)
        if store_serializer.is_valid():
            store_serializer.save()
            return JsonResponse("Agregado satisfactoriamente", safe=False)
        return JsonResponse("Ocurrio un error", safe=False)

