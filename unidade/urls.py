from django.urls import path
from .views import cadastro_unidade, listagem_unidade

urlpatterns = [
    path('cadastro/', cadastro_unidade, name='url_cadastro_unidade'),
    path('listagem/', listagem_unidade, name='url_listagem_unidade'),
]