from django.urls import path
from .views import cadastro_paciente, listagem_paciente

urlpatterns = [
    path('cadastro/', cadastro_paciente, name='url_cadastro_paciente'),
    path('listagem/', listagem_paciente, name='url_listagem_paciente'),
]