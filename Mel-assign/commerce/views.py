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
def signup_view(request):
    signup_text = "Sign up for our website"
    return render(request, 'signup.html', {'signup_text': signup_text})
def product(request):
    product_title = "This is the news page"
    product_content = "Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents."