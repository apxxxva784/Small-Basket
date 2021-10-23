from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home/homepage.html')

def products(request):
    return render(request,'home/products.html')    
