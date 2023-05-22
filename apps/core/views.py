from django.shortcuts import render
from django.core.paginator import Paginator

from apps.store.models import Product
from apps.store.cart import Cart

def borrame(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'core/mainpage.html')

def mainpage(request):
    products = Product.objects.all().reverse()
    cart = Cart(request)
    p = Paginator(products, 9)
    
    page_number = request.GET.get('page')
    try:
         page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    return render(request, 'core/mainpage.html', {
        'cart' : cart,
        'page_obj' : page_obj,
    })

def about(request):
    return render(request, 'core/about.html')

def info(request):
    return render(request, 'core/info.html')
