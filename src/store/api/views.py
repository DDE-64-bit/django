from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from base.models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self, request, pk):
        if pk == None:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            
            return Response(serializer.data)
        else:
            try:
                products = Product.objects.get(id=pk)
                serializer = ProductSerializer(products, many=False)
            except Product.DoesNotExist:
                return Response({"detail": "product not found"}, status=404)
            except Exception as e:
                return Response({"detail": "Unknown server error", "error": str(e)}, status=500)
            
            return Response(serializer.data)

class AddProduct(APIView):
    def post(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=201)
        return Response(serializer.errors, status=400)


"""
{
    "name":"book",
    "description": "book"
}
"""