from django.shortcuts import render
from .import models


def index(request):
    professores = models.Professor.objects.all()
    return render(request,'index.html', {'professores':professores})

"""""
def teste(request):
    professores = models.Professor.objects.all()

    return render(request,'index.html', {'professores':professores})
"""