from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'sistemaacademico/login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
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