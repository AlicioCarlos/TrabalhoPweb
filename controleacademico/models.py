from django.db import models

class Aluno(models.Model):
    user = models.ForeignKey('auth.User')
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()

    def __str__(self):
        return self.nome

class Professor(models.Model):
    user = models.ForeignKey('auth.User')
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()

    def __str__(self):
        return self.nome