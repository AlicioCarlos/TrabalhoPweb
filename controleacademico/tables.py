import django_tables2 as tables
from .models import Professor
from .models import Aluno
from .models import Boletim
from .models import Disciplina

class ProfessorTable(tables.Table):
     class Meta:
        model = Professor

class AlunoTable(tables.Table):
    class Meta:
        model = Aluno

class BoletimTable(tables.Table):
    class Meta:
        model = Boletim

class DisciplinaTable(tables.Table):
    class Meta:
        model = Disciplina