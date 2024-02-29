from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def home(requests):
    info = CompanyInformation.objects.all().first()
    products = Product.objects.all()

    data = {
        'info':info,
        'products':products
    }

    return render(requests, 'home.html', data)

def about(requests):
    return render(requests, 'about.html')

def contacts(requests):
    return render(requests, 'contact.html')
