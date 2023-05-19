from django.urls import path
from apps.store.views import product_detail, category_detail, search, add_to_cart, cart_view, remove_from_cart, change_quantity

urlpatterns = [
    path('search/', search, name='search'),
    path('add-to-cart/<str:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('change-quantity/<str:product_id>/', change_quantity, name='change_quantity'),
    path('cart/', cart_view, name='cart_view'),
    path('<slug:slug>/', category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
]

