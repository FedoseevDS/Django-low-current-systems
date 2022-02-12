from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('object', object, name='object'),
    path('about', about, name='about'),
    path('price', price, name='price'),
    path('client', client, name='client')
]