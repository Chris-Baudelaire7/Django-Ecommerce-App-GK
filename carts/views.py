from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from store.models import Product
from .models import Cart, CartItem


def _cart_id(request):
    
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
        
    return cart


def add_cart(request, product_id):
    
    product = Product.objects.get(id=product_id)
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        
    cart.save()
    
    try:
        cartitem = CartItem.objects.get(product=product, cart=cart)
        cartitem.quantity += 1
        cartitem.save()
    except CartItem.DoesNotExist:
        cartitem = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1
        )
        cartitem.save()
        
    return redirect("cart")


def remove_cart(request, product_id):
    
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        
    else:
        cart_item.delete()
        
    return redirect("cart")


def remove_cart_item(request, product_id):
    
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    
    cart_item.delete()
        
    return redirect("cart")


def cart(request, total=0, quantity=0, cart_items=None):
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
            
        tax = round((2 * total) / 100)
        grant_total = total + tax
            
    except CartItem.DoesNotExist:
        pass
    
    context = {
        "total": total,
        "quantity": quantity,
        "cart_items": cart_items,
        "tax": tax,
        "grant_total": grant_total
    }
    
    return render(request, "store/cart.html", context)