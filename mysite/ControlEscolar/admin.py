from django.contrib import admin
from mysite.ControlEscolar.models import *
# Register your models here.
admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)