from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    index_page = Main_page.objects.all()
    return render(request, 'main/index.html', {'index_page': index_page, 'title': 'Главная страница'})

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})

def price(request):
    return render(request, 'main/price.html', {'title': 'Цены'})

def client(request):
    return render(request, 'main/client.html', {'title': 'Клиенты'})

def contact(request):
    return render(request, 'main/contact.html', {'title': 'Контакты'})

def object(request):
    return render(request, 'main/object.html', {'title': 'Объекты'})