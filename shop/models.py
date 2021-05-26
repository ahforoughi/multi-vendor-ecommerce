from __future__ import unicode_literals

from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateTimeCheckMixin, DateTimeField, PositiveBigIntegerField, PositiveIntegerField

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=200)
    price = models.PositiveBigIntegerField()
    shop_id = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField()
    description = models.CharField(max_length=500)
    state = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f"{self.name} - {self.shop_id} - {self.state}"


