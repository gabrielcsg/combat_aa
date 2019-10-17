from django.urls import path
from .views import cadastro_paciente

urlpatterns = [
    path('cadastro/', cadastro_paciente, name='url_cadastro_paciente')
]