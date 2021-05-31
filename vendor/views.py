import vendor
from django import forms
from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Vendor
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def vendor_register(request):

    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor = Vendor.objects.create(
                name=user.name, 
                created_by=user
            )
            print (f"{vendor} submitted!")
        else:
            print ("Form is not valid")
            #print (form)
    else: 
        form = UserCreationForm()
        print("empty form created")
    
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)