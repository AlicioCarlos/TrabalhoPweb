from django.contrib import admin
from .models import Aluno
from .models import Professor
from .models import Disciplina
from .models import Turma
from .models import PeriodoLetivo
from .models import Boletim

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Boletim)
admin.site.register(PeriodoLetivo)
