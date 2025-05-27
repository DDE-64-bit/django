from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product

class GetProducts(APIView):
    def get(self, request, pk=None):
        if pk == None:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            
            return Response(serializer.data)
        else:
            try:
                product = Product.objects.get(id=pk)
                serializer = ProductSerializer(product, many=False)
                
                return Response(serializer.data)
            except Exception as e:
                return Response({"details": "Unknown error", "error": f"{e}"})

class AddProduct(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)