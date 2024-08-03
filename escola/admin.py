from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'rg', 'cpf', 'data_nascimento', )
    list_display = ('nome', 'rg', 'cpf', 'data_nascimento', )
    list_display_links = ('nome', 'rg', 'cpf', 'data_nascimento', )
    list_per_page = 20


class CursoAdmin(admin.ModelAdmin):
    search_fields = ('codigo_curso', 'descricao', 'nivel', )
    list_display = ('codigo_curso', 'descricao', 'nivel', )
    list_display_links = ('codigo_curso', 'descricao', 'nivel', )
    list_per_page = 20

class MatriculaAdmim(admin.ModelAdmin):
    list_display = ('periodo', 'aluno', 'curso', )
    list_display_links = ('periodo', 'aluno', 'curso', )
    list_per_page = 20


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmim)
