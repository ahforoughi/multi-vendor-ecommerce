from django.db.models import Q
from django.http import Http404
from django.http import JsonResponse
from json import JSONEncoder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

logger = logging.getLogger('django')

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404        

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)        
        logger.info(f'product {product} found')
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404        

    def get(self, request, category_slug):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)        
        logger.info(f'category {category} found!')
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

#TODO: figure out how to test this with postman 
    if query:
        print(query)
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
