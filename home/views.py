from django.http import HttpResponse
from django.shortcuts import render
from home.models import Category, Product
from cart.models import Cart, CartItem
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db import connection

def home(request):
    category_ids= Category.objects.all()
    return render(request,'home/homepage.html', {'categories':category_ids} )

def products(request, category):
    products= Product.objects.all()
    
    try:
        cart = Cart.objects.get(user = request.user)
        cartitems = CartItem.objects.filter(cart = cart)
    except:
        cartitems = None
    return render(request,'home/products.html', {'products':products, 'selected_category':category, 'items' : cartitems})    

def cart(request):
    cartitem = CartItem.objects.all()
    cart = Cart.objects.get(user = request.user)
    length = len(CartItem.objects.filter(cart=cart).exclude(quantity=0)) > 0
    return render(request,'home/cart.html', {'cartitem': cartitem, 'cart':cart, 'list' : length})

def checkout(request):
    cart = Cart.objects.get(user = request.user)
    return render(request, 'home/checkout.html', {'cart': cart})

def coredirect(request):
    cart = Cart.objects.get(user = request.user)
    with connection.cursor() as cursor:
        cursor.execute("DELETE from cart_cartitem where cart_id = %s ", [cart.id])
    cart.total = 0
    cart.save()

    return redirect("/")