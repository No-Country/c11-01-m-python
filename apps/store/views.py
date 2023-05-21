from django.shortcuts import render, get_object_or_404, redirect
from apps.store.models import Product, Category, Order, OrderItem
from apps.store.cart import Cart
from apps.store.forms import OrderForm
from apps.account.models import Account

#Decoradores
from django.contrib.auth.decorators import login_required
#Carrito
def add_to_cart(request, product_id, quantity):
    cart = Cart(request)
    quantity = int(quantity)
    print(cart)
    cart.add(product_id, quantity)  
    return redirect('/')

#Agregar cantidad variable en el detalle 
def add_quantity(request, product_id):
    query = int(request.GET.get('query', ''))
    cart = Cart(request)
    quantity = int(query)
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

@login_required
def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            total_price = 0

            for item in cart:
                product = item['product']
                total_price += product.price_product * int(item['quantity'])

            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = total_price
            order.save()

            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price_product * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()

            return redirect('/store/invoice/' + str(order.id))
    else:
        form = OrderForm()

    return render(request, 'store/checkout.html', {
        'cart': cart,
        'form': form,
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

#Ventana de Gracias
def invoice(request, pk):
    order = get_object_or_404(Order, pk = pk)
    orderitems = OrderItem.objects.filter(order = pk).distinct()
    return render(request, 'store/invoice.html', {
        'order' : order,
        'orderitems' : orderitems
    })