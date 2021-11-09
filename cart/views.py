from django.http.response import HttpResponse
from django.http import HttpResponseRedirect  
from django.shortcuts import redirect, render
from home.models import Product
from .models import CartItem, Cart

def add_to_cart(request):
    id = request.POST.get('id')
    item = Product.objects.get(p_id=id)

    if request.user.is_authenticated: #user logged in
        try:
            cart = Cart.objects.get(user=request.user) #user cart exists
        except:
            cart = Cart.objects.create(user = request.user) #user cart doesnt exist and is hence created
        product = CartItem.objects.filter(product=item, cart=cart) #looks for item in the cart
        if item.stock>=1:
            if product: #product already present in cart
                product = product[0]
                product.quantity += 1
                product.price += item.price
                cart.total += item.price
                product.save()
                item.stock -= 1
                item.save()
                cart.save()

            else: #product not in cart
                new_item = CartItem(product=item, price=item.price, quantity=1, cart=cart)
                cart.total += new_item.price
                new_item.save()
                item.stock -= 1
                item.save()
                cart.save()
            response = HttpResponse(status=201)
        else:
            pass
    return response


def remove_from_cart(request):
    id = request.POST.get('id')
    item = Product.objects.get(p_id=id)

    cart = Cart.objects.get(user=request.user)
    product = CartItem.objects.filter(product=item, cart=cart)
    product = product[0]
    if product.quantity<=0:
        CartItem.objects.filter(product=item, cart=cart).delete()
        product.save()
    else:
        product.quantity -= 1
        product.price -= item.price
        cart.total -= item.price
        product.save()
        item.stock += 1
        item.save()
        cart.save()

    cartitem = CartItem.objects.all()
    cart = Cart.objects.get(user = request.user)
    return render(request,'home/cart.html', {'cartitem': cartitem, 'cart':cart})