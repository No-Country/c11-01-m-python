from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('', include('apps.core.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'apps.core.views.error_400'
handler403 = 'apps.core.views.error_403'
handler404 = 'apps.core.views.error_404'
handler505 = 'apps.core.views.error_505'

admin.site.site_header  =  "Administración de Crazy Vegan"  
admin.site.site_title  =  "Pagina de Administración de Crazy Vegan"
admin.site.index_title  =  "Administración de Crazy Vegan"