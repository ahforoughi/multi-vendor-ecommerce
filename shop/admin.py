from django.contrib import admin

from .models import Product, Token

admin.site.register(Product)
admin.site.register(Token)

