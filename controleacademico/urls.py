from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'professor/', views.professor, name='professor'),
    url(r'aluno/', views.aluno, name='aluno'),
    url(r'boletim/', views.boletimDoAluno, name='boletim'),
    url(r'historico/', views.historicoDoAluno, name='historico'),
    url(r'graficoDesenpenho/', views.graficoDesenpenho, name='graficoDesenpenho'),
    url(r'disciplinas/(?P<pk>\d+)/$', views.disciplinas,  name='disciplinas'),
    url(r'acessonegado/', views.acessonegado, name='acessonegado'),

    #url(r'turma/', views.turma, name='turma'),
    #url(r'^turmaDetalhes/(?P<prof_mat>[0-9]+)/$', views.turmaDetalhes, name='turmaDetalhes'),
]