from django.db import models

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    idade = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='pets/', blank=True, null=True)

    def __str__(self):
        return self.nome