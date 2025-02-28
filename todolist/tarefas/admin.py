from django.contrib import admin
from .models import Usuario, Equipe, Categoria, Tarefa, Comentario, UsuarioEquipe, Responsavel, TarefaCategoria

admin.site.register(Usuario)
admin.site.register(Equipe)
admin.site.register(Categoria)
admin.site.register(Tarefa)
admin.site.register(Comentario)
admin.site.register(UsuarioEquipe)
admin.site.register(Responsavel)
admin.site.register(TarefaCategoria)
