from django.urls import path
from apps.store.views import product_detail

urlpatterns = [
    path('<slug:slug>/', product_detail, name='product_detail'),
]

