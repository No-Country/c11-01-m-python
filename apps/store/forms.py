from django import forms
from .models import Product, Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'receiver', 'receiver_address', 'paid_method', 'paid_account')