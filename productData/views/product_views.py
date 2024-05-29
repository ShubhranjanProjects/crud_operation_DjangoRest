from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from productData import models
from productData.serializers import ProductSerializers

class GetProducts(APIView):
    def get(self, request):
        products = models.Products.objects.all()
        response = ProductSerializers(products, many=True)
        return Response(response.data)

class CreateProducts(APIView):
    def post(self, request):
        product_request = request.data
        product_data = ProductSerializers(data=product_request)
        if product_data.is_valid():
            product_data.save()
            return Response({'msg': "received"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': product_data.errors}, status=status.HTTP_400_BAD_REQUEST)

class GetProduct(APIView):
    def get(self, request, pk):
        product = get_object_or_404(models.Products, id=pk)
        response = ProductSerializers(product, many=False)
        return Response(response.data)

class DeleteProduct(APIView):
    def delete(self, request, pk):
        product = get_object_or_404(models.Products, id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateProduct(APIView):
    def put(self, request, pk):
        product = get_object_or_404(models.Products, id=pk)
        product_data = ProductSerializers(product, data=request.data)
        if product_data.is_valid():
            product_data.save()
            return Response(product_data.data)
        return Response(product_data.errors, status=status.HTTP_400_BAD_REQUEST)
