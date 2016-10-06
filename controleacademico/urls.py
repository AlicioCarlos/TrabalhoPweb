from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'professor/', views.professor),
    url(r'disciplinas/', views.disciplinas),
]