from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/vendor/$', views.vendor_register, name='vendor_register')
]