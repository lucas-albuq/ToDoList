from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tarefas.models import Equipe, UsuarioEquipe

@login_required
def home(request):
    equipes = Equipe.objects.filter(usuarioequipe__usuario=request.user)

    return render(request, 'home.html', {'equipes': equipes})
