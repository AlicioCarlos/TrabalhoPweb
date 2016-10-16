from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/$', auth_views.login, {'template_name': 'sistemaacademico/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'sistemaacademico/logout.html'}, name='logout'),
    url(r'professor/', views.professor, name='professor'),
    url(r'aluno/', views.aluno, name='aluno'),
    url(r'boletim/', views.boletimDoAluno, name='boletim'),
    url(r'historico/', views.historicoDoAluno, name='historico'),
    url(r'graficoDesenpenho/', views.graficoDesenpenho, name='graficoDesenpenho'),
    url(r'turmaDetalhes/(?P<pk>\d+)/$', views.turmaDetalhes,  name='turmaDetalhes'),
    url(r'acessonegado/', views.acessonegado, name='acessonegado'),
    url(r'relatorio_alunos_turma_xls/(?P<pk>\d+)/$', views.relatorio_alunos_turma_xls, name='relatorio_alunos_turma_xls'),
    url(r'relatorio_boletim_xls/$', views.relatorio_boletim_xls, name='relatorio_boletim_xls'),
    url(r'relatorio_Historico_xls/$', views.relatorio_Historico_xls, name='relatorio_Historico_xls'),


    #url(r'turma/', views.turma, name='turma'),
    #url(r'^turmaDetalhes/(?P<prof_mat>[0-9]+)/$', views.turmaDetalhes, name='turmaDetalhes'),
]