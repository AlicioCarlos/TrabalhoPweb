from django.db import models

class Aluno(models.Model):
    nome = models.ForeignKey('auth.User')
    matricula = models.IntegerField()

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.ForeignKey('auth.User')
    matricula = models.IntegerField()

    def __str__(self):
        return self.nome