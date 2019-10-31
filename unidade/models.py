from django.db import models


class Unidade(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.nome