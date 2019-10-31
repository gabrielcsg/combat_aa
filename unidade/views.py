import requests
from django.shortcuts import render, redirect
from .form import CadastroUnidadeForm
from .models import Unidade


def listagem_unidade(request):
    data = {}
    data['unidades'] = Unidade.objects.all()
    return render(request, 'listagem_unidades.html', data)


def cadastro_unidade(request):
    form = CadastroUnidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form_unidade.html', {'form': form})


