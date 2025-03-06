from django.shortcuts import render, get_object_or_404
from tarefas.models import Equipe

def equipe_detalhes(request, id):
    equipe = get_object_or_404(Equipe, id=id)
    return render(request, 'equipe/equipe_detalhes.html', {'equipe': equipe})
