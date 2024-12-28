from django.shortcuts import render
from math import ceil

from django.http import HttpResponse
from blog.models import Blogpost
from shop.models import Product

def index(request):
    myposts = Blogpost.objects.all()
    products= Product.objects.all()

    return render(request, 'indexf.html',{'myposts': myposts, 'products':products})

