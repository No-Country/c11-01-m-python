from django.shortcuts import render

from apps.store.models import Product

def mainpage(request):
    products = Product.objects.all()[0:6]

    return render(request, 'core/mainpage.html', {
        'products': products
    })

def about(request):
    return render(request, 'core/about.html')

def info(request):
    return render(request, 'core/info.html')
