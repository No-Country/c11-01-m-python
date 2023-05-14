from django.urls import path
from .views import mainpage, about, info

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('about/', about, name='about'),
    path('info/', info, name='info'),
]

