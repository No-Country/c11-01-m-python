from django.urls import path, include
from .views import mainpage, about, info, product

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('product/', product, name='product'),
    path('about/', about, name='about'),
    path('info/', info, name='info'),
    path('', include('apps.store.urls')),
]

