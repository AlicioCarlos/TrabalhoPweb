from django.shortcuts import render
from .import models
from .tables import ProfessorTable
from .tables import TurmaTable

def index(request):
    queryset = models.Professor.objects.all()
    table = ProfessorTable(queryset)
    return render(request,'index.html', {'table':table})

def disciplinas(request):
    return render(request, 'disciplinas.html')


def professor(request):
    queryset = models.Turma.objects.all()
    table = TurmaTable(queryset)
    return render(request, 'professor.html', {'table':table})