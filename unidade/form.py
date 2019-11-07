from django.forms import ModelForm

from .models import Unidade


class CadastroUnidadeForm(ModelForm):
    class Meta:
        model = Unidade
        fields = ['nome', 'endereco']