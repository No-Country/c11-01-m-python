from django.urls import path, include
from .views import mainpage, about, info, product, offer

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('product/', product, name='product'),
    path('offer/', offer, name='offer'),
    path('about/', about, name='about'),
    path('info/', info, name='info'),
    path('', include('apps.store.urls')),
]

