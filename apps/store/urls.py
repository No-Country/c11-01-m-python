from django.urls import path
from apps.store.views import product_detail, category_detail

urlpatterns = [
    path('<slug:slug>/', category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
]

