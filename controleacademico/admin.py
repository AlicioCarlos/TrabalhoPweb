from django.contrib import admin
from .models import Aluno
from .models import Professor

admin.site.register(Aluno)
admin.site.register(Professor)
