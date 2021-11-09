from django.http import HttpResponse
from django.shortcuts import render
from home.models import Category, Product

def home(request):
    category_ids= Category.objects.all()
    return render(request,'home/homepage.html', {'categories':category_ids} )

def products(request, category):
    products= Product.objects.all()
    return render(request,'home/products.html', {'products':products, 'selected_category':category})    

def cart(request):
    return render(request,'home/cart.html')