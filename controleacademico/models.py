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

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    cargaHoraria = models.IntegerField()

    def __str__(self):
        return self.nome

class Turma(models.Model):
    codigo = models.CharField(max_length=20)
    professor = models.ForeignKey(Professor)
    disciplina = models.ForeignKey(Disciplina)
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.codigo

class Boletim(models.Model):
    aluno = models.ForeignKey(Aluno)
    disciplina = models.ForeignKey(Disciplina)
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    nota3 = models.FloatField()

    def __str__(self):
        return self.aluno

    def media(self):
        return (self.nota1 + self.nota2 + self.nota3)/3