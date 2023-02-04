import status
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api.models import Product, Category
from api.serializer import ProductSerializer, CategorySerializer, ProductMSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == "GET":
        product = Product.objects.select_related('category').all()
        product_serializer = ProductMSerializer(product, many=True, context={'request': request})
        return Response(product_serializer.data)
    elif request.method == "POST":
        product = ProductMSerializer(data=request.data)
        product.is_valid(raise_exception=True)
        product.save()
        return Response(product.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "GET":
        product_serializer = ProductMSerializer(product)
        return Response(product_serializer.data)
    elif request.method == "PUT":
        product_serializer = ProductMSerializer(product, data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "PATCH":
        product_serializer = ProductMSerializer(product, data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        product.delete()
        product.save()
        return Response(status=status.HTTP_200_OK)


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
