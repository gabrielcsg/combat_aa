import requests
from django.shortcuts import render, redirect
from .form import CadastroPacienteForm
from .models import Paciente


def listagem_paciente(request):
    data = {}
    data['pacientes'] = Paciente.objects.all()
    return render(request, 'listagem_pacientes.html', data)

def cadastro_paciente(request):
    form = CadastroPacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form})
