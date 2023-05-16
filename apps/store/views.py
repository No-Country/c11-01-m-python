from django.shortcuts import render
from apps.store.models import Product

def product_detail(request, slug):
    product = Product.objects.get(slug = slug)
    return render(request, 'store/product_detail.html', {
        'product' : product
    })
