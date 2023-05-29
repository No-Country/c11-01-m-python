from django.conf import settings

from .models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        
        for item in self.cart.values():
            item['total_price'] = float(item['product'].price_product * item['quantity']) / 100

            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity, update_quantity=False):
        product_id = str(product_id)
        quantity = int(quantity)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': int(quantity), 'id': product_id}

        #Los productos no deben de pasar de 10 en cantidad para evitar compras mayoristas via ecommerce
        elif product_id == product_id:
            self.cart[product_id]['quantity'] += int(quantity)
            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
            elif self.cart[product_id]['quantity'] > 10:
                self.cart[product_id]['quantity'] = 10
        self.save()
    
    def remove(self, product_id):
        if str(product_id) in self.cart:
            self.cart.pop(str(product_id))
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)   
        return float(sum(item['product'].price_product * item['quantity'] for item in self.cart.values()))