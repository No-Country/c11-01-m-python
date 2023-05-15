from django.db import models
from apps.helper.utilities import pkgen

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
    name_category = models.ForeignKey(Category, on_delete=models.CASCADE)
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





    
