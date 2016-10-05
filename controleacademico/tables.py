from .models import Professor
import django_tables2 as tables

class ProfessorTable(tables.Table):
     class Meta:
        model = Professor