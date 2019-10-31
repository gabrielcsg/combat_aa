from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('paciente/', include('paciente.urls')),
    path('unidade/', include('unidade.urls')),
]
