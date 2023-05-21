from django.shortcuts import render

from apps.store.models import Product
from apps.store.cart import Cart

def borrame(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'core/mainpage.html')
def mainpage(request):
    products = Product.objects.all()[0:6]
    cart = Cart(request)
    return render(request, 'core/mainpage.html', {
        'products': products,
        'cart' : cart
    })

def about(request):
    return render(request, 'core/about.html')

def info(request):
    return render(request, 'core/info.html')
