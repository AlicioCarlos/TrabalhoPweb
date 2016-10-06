from .models import Professor
from .models import Turma
import django_tables2 as tables

class ProfessorTable(tables.Table):
     class Meta:
        model = Professor


class TurmaTable(tables.Table):
    class Meta:
        model = Turma