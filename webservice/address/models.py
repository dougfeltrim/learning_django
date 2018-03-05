from django.db import models

class Cidade(models.Model):
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    cep = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
