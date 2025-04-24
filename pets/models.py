from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    idade = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='pets/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

class SolicitacaoAdocao(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    nome_pessoa = models.CharField(max_length=100)
    idade_pessoa = models.IntegerField()
    endereco = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome_pessoa} quer adotar {self.pet.nome}'