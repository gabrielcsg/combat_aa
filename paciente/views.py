import requests
from django.shortcuts import render
from .form import CadastroPacienteForm


def cadastro_paciente(request):
    if request.method == 'POST':
        form = CadastroPacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form.html')
    else:
        form = CadastroPacienteForm()
        return render(request, 'form.html', {'form': form})
