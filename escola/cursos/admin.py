from django.contrib import admin

# Register your models here.
from .models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'publicacao', 'atualizacao', 'is_ativo')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ( 'curso', 'nome', 'email', 'avaliacao', 'publicacao', 'atualizacao', 'is_ativo' )