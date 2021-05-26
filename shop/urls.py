from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/product/$', views.submit_product, name='submit_product')
]