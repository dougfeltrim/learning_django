from django.db import models

class Local(models.Model):
    logradouro = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    cep = models.IntegerField(default=0)
