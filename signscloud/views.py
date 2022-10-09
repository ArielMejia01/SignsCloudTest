
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

#Importar los modelos y las clases serializadoras
from signscloud.models import Stores, Brands, Deals
from signscloud.serializers import StoreSerializer, BrandSerializer, DealSerializer

#modulo de almacenamiento determinado
#from django.core.files.storage import default_storage

# Create your views here.
# vamos a obtner todas las tiendas
@csrf_exempt
@api_view(['GET'])
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
    return Response(storeApi)
@csrf_exempt  
def brandApi(request, id=0):
    if request.method=='GET':
        brand = Brands.objects.all()
        brand_serializer = BrandSerializer(brand, many=True)
        return JsonResponse(brand_serializer.data, safe=False)
    elif request.method=='POST':
        brand_data = JSONParser().parse(request)
        brand_serializer = BrandSerializer(data=brand_data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return JsonResponse("Agregado satisfactoriamente", safe=False)
        return JsonResponse("Ocurrio un error", safe=False)
@csrf_exempt  
def dealApi(request, id=0):
    if request.method=='GET':
        deal = Deals.objects.all()
        deal_serializer = DealSerializer(deal, many=True)
        return JsonResponse(deal_serializer.data, safe=False)
    elif request.method=='POST':
        deal_data = JSONParser().parse(request)
        deal_serializer = DealSerializer(data=deal_data)
        if deal_serializer.is_valid():
            deal_serializer.save()
            return JsonResponse("Agregado satisfactoriamente", safe=False)
        return JsonResponse("Ocurrio un error", safe=False)

#Guardar el archivo image y retornar en json el nombre de la imagen
"""@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)
    
class ImagenJson(brandApi):
    def get(self, request, *args):
        print(str(self.parser_classes))
        return JsonResponse({'parsers': ' '.join(map(str, self.parser_classes))}, status=204)
"""


        