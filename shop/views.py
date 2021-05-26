from django.shortcuts import render
from .models import Token, Product, User    
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from json import JSONEncoder
from django.http import JsonResponse
import time


# TODO: validate data
@csrf_exempt
def submit_product(request):
    """user submit a product"""
    
    if 'date' not in request.POST:
        now = datetime.now()
    
    this_token = request.POST['token']
    this_seller = User.objects.filter(token__token = this_token).get()
    this_price = request.POST['price']

    Product.objects.create(
        seller = this_seller, 
        price = this_price, 
        creation_date = now
    )

    print ("Product submitted!")
    return JsonResponse({
            'status': 'ok',
        }, encoder=JSONEncoder)
