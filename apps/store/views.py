from django.shortcuts import render, get_object_or_404, redirect
from apps.store.models import Product, Category
from apps.store.cart import Cart
#Carrito
def add_to_cart(request, product_id, quantity):
    cart = Cart(request)
    cart.add(product_id, quantity)  
    return redirect('/')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(str(product_id))
    return redirect('/')

def change_quantity(request, product_id):
    action = request.GET.get('action', '')
    if action:
        quantity = 1
        if action == 'decrease':
            quantity = -1
        cart = Cart(request)
        cart.add(product_id, quantity, True)
    
    return redirect('/')

def cart_view(request):
    cart = Cart(request)
    return render(request, 'store/cart_view.html', {
        'cart': cart
    })
#fin del carrito
def category_detail(request, slug):
    category = get_object_or_404(Category, slug = slug)
    products = category.products.all()
    return render(request, 'store/category_detail.html', {
        'category' : category,
        'products' : products
    })

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug = slug)
    return render(request, 'store/product_detail.html', {
        'product' : product
    })

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name_product__icontains=query)
    return render(request, 'store/search.html', {
        'query':query,
        'products': products
    })

