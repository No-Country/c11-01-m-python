from django.urls import path

from apps.users.views import user_detail, signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('<int:pk>/', user_detail, name='users_detail'),
]
