from django.db.models import Q
from django.http import Http404
from django.http import JsonResponse
from json import JSONEncoder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
from .models import Product, Category
from .serializers import ProductSerializer

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
        logger.info(f'product {product} found!!!!')
        return Response(serializer.data)


