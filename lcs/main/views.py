from django.shortcuts import render

# Create your views here.

menu = [{'title': ''}

]

def index(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def object(request):
    return render(request, 'main/object.html')