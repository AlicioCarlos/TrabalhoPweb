import django_tables2 as tables
from .models import Professor
from .models import Aluno
from .models import Boletim
from .models import Turma
from .models import Disciplina

class ProfessorTable(tables.Table):
     class Meta:
        model = Professor
        exclude = ('id',)


class AlunoTable(tables.Table):
    class Meta:
        model = Aluno
        exclude = ('id',)


class DisciplinaTable(tables.Table):
    class Meta:
        model = Disciplina
        exclude = ('id',)


class TurmaTable(tables.Table):
    class Meta:
        model = Turma
        exclude = ('id',)


class BoletimTable(tables.Table):
    class Meta:
        model = Boletim
        exclude = ('id','aluno')