from django.forms import ModelForm

from paciente.models import Paciente


class CadastroPacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'tipo_sanguineo', 'sexo', 'endereco', 'patologia', 'telefone']
