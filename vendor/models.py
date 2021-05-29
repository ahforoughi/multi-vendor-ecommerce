from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    name =  models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']