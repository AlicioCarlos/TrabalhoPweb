from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .boletim_xls import WriteToExcel
from .models import Professor
from .models import Aluno
from .models import Boletim
from .models import Turma
from .models import Disciplina
from .models import PeriodoLetivo
from .tables import BoletimTable
from .tables import AlunosTurmaTable


@login_required
def professor(request):
    usuarioLogado = request.user
    professor = Professor.objects.get(nome=usuarioLogado)
    periodoLetivo = PeriodoLetivo.objects.last()
    turmas = Turma.objects.filter(professor__nome=usuarioLogado, periodoLetivo__nome=periodoLetivo)
    return render(request, 'sistemaacademico/professor.html',
                  {'turmas': turmas, 'professor': professor, 'periodoLetivo': periodoLetivo})

@login_required
def aluno(request):
    alunologado = request.user
    aluno = Aluno.objects.get(nome=alunologado)
    periodoLetivo = PeriodoLetivo.objects.last()
    turmas = Turma.objects.filter(alunos__nome=alunologado, periodoLetivo__nome=PeriodoLetivo.objects.last())
    return render(request, 'sistemaacademico/aluno.html', {'turmas': turmas, 'aluno': aluno, 'periodoLetivo': periodoLetivo})


@login_required
def boletimDoAluno(request):
    aluno = Aluno.objects.filter(nome=request.user)
    boletimAluno = Boletim.objects.filter(aluno=aluno, turma__periodoLetivo__nome=PeriodoLetivo.objects.last())
    table = BoletimTable(boletimAluno)
    return render(request, 'sistemaacademico/boletim.html', {'table':table})


@login_required
def historicoDoAluno(request):
    aluno = Aluno.objects.filter(nome=request.user)
    boletimAluno = Boletim.objects.filter(aluno=aluno).order_by('-semestre')
    table = BoletimTable(boletimAluno)
    return render(request, 'sistemaacademico/historico.html', {'table':table})


@login_required
def turmaDetalhes(request, pk):
    boletins = Boletim.objects.filter(turma_id=pk)
    table = AlunosTurmaTable(boletins)
    return render(request, 'sistemaacademico/turmaDetalhes.html', {'table': table, 'turma_id': pk})


@login_required
def graficoDesenpenho(request):
    boletins = Boletim.objects.all()
    disiplinas = Disciplina.objects.all()
    media = 0.0
    historico = []
    for disiplina in disiplinas:
        for boletim in boletins:
            if boletim.disciplina.pk == disiplina.pk:
                historico.append(boletim.media)

        media = 0.0

    return render(request, 'sistemaacademico/graficoDesenpenho.html', {'disiplinas':disiplinas})


def acessonegado(request):
    return render(request, 'sistemaacademico/acessonegado.html')


@login_required
def index(request):
    usuarioLogado = request.user

    if Professor.objects.filter(nome=usuarioLogado):
        professor = Professor.objects.get(nome=usuarioLogado)
        periodoLetivo = PeriodoLetivo.objects.last()
        turmas = Turma.objects.filter(professor__nome=usuarioLogado, periodoLetivo__nome=periodoLetivo)
        return render(request, 'sistemaacademico/professor.html',
                      {'turmas': turmas, 'professor': professor, 'periodoLetivo':periodoLetivo})

    if Aluno.objects.filter(nome=usuarioLogado):
        aluno = Aluno.objects.get(nome=usuarioLogado)
        periodoLetivo = PeriodoLetivo.objects.last()
        turmas = Turma.objects.filter(alunos__nome=usuarioLogado, periodoLetivo__nome=periodoLetivo)
        return render(request, 'sistemaacademico/aluno.html',
                      {'turmas': turmas, 'aluno': aluno, 'periodoLetivo':periodoLetivo})


@login_required
def relatorio_alunos_turma_xls(request, pk):
    turma = Turma.objects.get(pk=pk)
    boletins = Boletim.objects.filter(turma_id=pk)
    report = [boletim.boletimProfessor_json() for boletim in boletins]
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
    keysColunas = ['aluno', 'nota1', 'nota2', 'nota3', 'media']
    xlsx_data = WriteToExcel(report, keysColunas, "TURMA", turma.nome,
                             ('PROFESSOR: ' + Professor.objects.get(nome=request.user).nome.upper()))
    response.write(xlsx_data)
    return response


@login_required
def relatorio_boletim_xls(request):
    boletins = Boletim.objects.filter(aluno__nome=request.user).filter(turma__periodoLetivo=PeriodoLetivo.objects.last())
    report = [boletim.boletimAluno_json() for boletim in boletins]
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
    keysColunas = ['disciplina', 'turma', 'nota1', 'nota2', 'nota3', 'media']
    xlsx_data = WriteToExcel(report, keysColunas,"BOLETIM", PeriodoLetivo.objects.last().nome,
                             ('ALUNO: '+Aluno.objects.get(nome=request.user).nome))
    response.write(xlsx_data)
    return response

@login_required
def relatorio_Historico_xls(request):
    boletins = Boletim.objects.filter(aluno__nome=request.user)
    report = [boletim.boletimAluno_json() for boletim in boletins]
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
    keysColunas = ['disciplina', 'turma','nota1', 'nota2', 'nota3', 'media']
    xlsx_data = WriteToExcel(report, keysColunas, "HISTÓRICO",  "",
                             ('ALUNO: '+Aluno.objects.get(nome=request.user).nome))
    response.write(xlsx_data)
    return response





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

    {% for key, value in historico.items %}
                <div style="margin-left: 10px;">
                    <h3><p>{{ key }}</p></h3>
                    <h4><p>Média: {{ value }}</p></h4>
                </div>
            {% endfor %}

"""