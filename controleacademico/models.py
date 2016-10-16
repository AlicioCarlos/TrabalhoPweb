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


class PeriodoLetivo(models.Model):
    nome = models.CharField(max_length=6)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    periodoLetivo = models.ForeignKey(PeriodoLetivo)
    disciplina = models.ForeignKey(Disciplina)
    professor = models.ForeignKey(Professor)
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return str(self.disciplina).upper() + " " + str(self.nome) + "-" + str(self.periodoLetivo.nome)


class Boletim(models.Model):
    aluno = models.ForeignKey(Aluno)
    turma = models.ForeignKey(Turma)
    semestre = models.IntegerField()
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    nota3 = models.FloatField()

    def __str__(self):
        return str(self.aluno) + " " + str(self.turma)

    def media(self):
        return ((self.nota1 + self.nota2 + self.nota3)/3)

    def boletimAluno_json(self):
        return {'disciplina': str(self.turma.disciplina.nome).upper(),
                'turma': str(self.turma.nome + " - " + self.turma.periodoLetivo.nome).upper(),
                'nota1': self.nota1, 'nota2': self.nota2,'nota3': self.nota3, 'media':self.media()}

    def boletimProfessor_json(self):
        return {'aluno': self.aluno.nome, 'nota1': self.nota1, 'nota2': self.nota2, 'nota3': self.nota3, 'media': self.media()}