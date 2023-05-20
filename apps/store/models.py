from django.db import models
from apps.helper.utilities import pkgen
from apps.account.models import Account

class Category(models.Model):
    id_category = models.CharField(max_length=8, primary_key=True, default=pkgen)
    name_category = models.CharField(max_length=255, null = False, unique=True)
    description_category = models.TextField(null = False)
    image_category = models.ImageField(blank=False, null=False, upload_to='Category')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def natural_key(self):
        return (self.id_category)
    
    def __str__(self):
        return self.name_category

class Product(models.Model):
    id_product = models.CharField(max_length=8, primary_key=True, default=pkgen)
    name_product = models.CharField(max_length=255, null=False)
    price_product = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description_product = models.TextField(null = False)
    stock_product = models.IntegerField(null = False)
    image_product = models.ImageField(blank=False, null=False, upload_to='Items/')
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name= 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.name_product

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255, blank=True, null=True)
    receiver_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    paid_method = models.CharField(max_length=255, null=True)
    paid_account = models.CharField(max_length=255, blank=True, null=True)
    merchant_id = models.CharField(max_length= 500)
    created_by = models.ForeignKey(Account, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount
        return 0

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.price








    
