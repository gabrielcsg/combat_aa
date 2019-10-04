from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    tipo_sanguineo = models.CharField(max_length=3)
    sexo = models.CharField(max_length=1)
    endereco = models.CharField(max_length=150)
    patologia = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
