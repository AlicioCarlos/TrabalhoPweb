from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Professor
from .models import Aluno
from .models import Boletim
from .models import Turma
from .models import Disciplina
from .tables import ProfessorTable
from .tables import BoletimTable
from .tables import AlunoTable
import json


def professor(request):
    professores = Professor.objects.all()
    turmas = Turma.objects.all()
    profesorlogado = request.user
    turmasProfessor = []
    for professor in professores:
        if professor.user == request.user:
            matricula = professor.matricula
            for i in range(len(turmas)):
                if turmas[i].professor.user == profesorlogado:
                    turmasProfessor.append(turmas[i])
            return render(request, 'sistemaacademico/professor.html', {'turmasProfessor': turmasProfessor, 'matricula': matricula})
    return render(request, 'sistemaacademico/acessonegado.html')


def aluno(request):
    alunos = Aluno.objects.all()
    boletins = Boletim.objects.all()
    alunologado = request.user
    boletimAluno = []
    for aluno in alunos:
        if aluno.user == alunologado:
            matricula = aluno.matricula
            for i in range(len(boletins)):
                if boletins[i].aluno.user == alunologado:
                    boletimAluno.append(boletins[i])
            return render(request, 'sistemaacademico/aluno.html', {'boletimAluno': boletimAluno, 'matricula': matricula})
    return render(request, 'sistemaacademico/acessonegado.html')


def boletimDoAluno(request):
    alunos = Aluno.objects.all()
    alunologado = request.user
    alunoPK = ""
    for aluno in alunos:
        if aluno.user == alunologado:
            alunoPK  = aluno.pk
    boletimAluno = Boletim.objects.filter(aluno = alunoPK)
    table = BoletimTable(boletimAluno.all())
    return render(request, 'sistemaacademico/boletim.html', {'table':table})


def historicoDoAluno(request):
    alunos = Aluno.objects.all()
    boletins = Boletim.objects.all()
    alunologado = request.user
    historico = {}
    for aluno in alunos:
        if aluno.user == alunologado:
            for i in range(len(boletins)):
                if boletins[i].aluno.user == alunologado:
                    historico[boletins[i].disciplina.nome] = boletins[i].media
    return render(request, 'sistemaacademico/historico.html', {'historico':historico})


def disciplinas(request, pk):
    disciplinas = Disciplina.objects.get(pk=pk)
    table = AlunoTable(disciplinas.alunos.all())
    return render(request, 'sistemaacademico/disciplinas.html', {'table' : table, 'disciplinaNome': disciplinas.nome})

def graficoDesenpenho(request):
    boletins = Boletim.objects.all()
    disiplinas = Disciplina.objects.all()
    data = ['X', 'Y', 'Z'];
    data1 = [1, 2, 3];

    media = 0.0
    historico = []
    for disiplina in disiplinas:
        for boletim in boletins:
            if boletim.disciplina.pk == disiplina.pk:
                historico.append(boletim.media)

        media = 0.0

    return render(request, 'sistemaacademico/graficoDesenpenho.html', {'data':json.dumps(data), 'data1':json.dumps(data1)})


def acessonegado(request):
    return render(request, 'sistemaacademico/acessonegado.html')




@login_required
def index(request):
        return render(request, 'sistemaacademico/index.html', {})

"""""
def index(request):
    professor_list = Professor.objects.order_by('-matricula')
    context = {'professor_list': professor_list}
    return render(request, 'index.html', context)


    def turma(request):
    queryset = Turma.objects.all()
    table = TurmaTable(queryset)
    return render(request, 'turma.html', {'table':table})


def turmaDetalhes(request, prof_mat):
    try:
        queryset = Turma.objects.filter(professor=prof_mat)
        table = TurmaTable(queryset.all())
    except Turma.DoesNotExist:
        raise Http404("Turma não Localizada!!")
    return render(request, 'turmaDetalhes.html', {'table': table})

"""