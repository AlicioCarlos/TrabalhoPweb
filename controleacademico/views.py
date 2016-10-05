from django.shortcuts import render
from .import models
from .tables import ProfessorTable

def index(request):
    queryset = models.Professor.objects.all()
    table = ProfessorTable(queryset)
    return render(request,'index.html', {'table':table})

def disciplinas(request):
    return render(request, 'disciplinas.html')

"""""
def teste(request):
    professores = models.Professor.objects.all()

    return render(request,'index.html', {'professores':professores})
"""