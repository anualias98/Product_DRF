from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.response import Response
from .models import Product
from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework.response import Response




# Create your views here.


@api_view(['Get'])
def api_overview(request):
    api_urls = {
        'List' : '/product-list',
        'Detail':'/product-detail/<int:id>',
        'Create':'/product-create/',
        'Update':'/product-update/<int:id>',
        'Delete':'/product-delete/<int:id>'
    }
    return Response(api_urls)

@api_view(['Get'])
def showall(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)
#create
@api_view(['POST'])
def createproduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#singleview
@api_view(['GET'])
def viewproduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
#update
@api_view(['POST'])
def updateproduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deleteproduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Product is deleted successfully")



