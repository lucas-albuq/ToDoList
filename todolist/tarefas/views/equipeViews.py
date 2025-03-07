from django.shortcuts import render, redirect, get_object_or_404
from tarefas.models import Equipe
from django.contrib import messages

class EquipeViews:
    def equipe_detalhes(request, id):
        equipe = get_object_or_404(Equipe, id=id)
        return render(request, 'equipe/equipe_detalhes.html', {'equipe': equipe})
    '''
    def criar_equipe(request):
        if request.method == 'POST':    
            nome = request.POST.get('nome', '').strip()
            descricao = request.POST.get('descricao', '').strip()
            foto_perfil = request.FILES.get('foto_perfil', None)
            foto_capa = request.FILES.get('foto_capa', None)
            
            if not nome:
                messages.error(request, "O nome da equipe é obrigatório.")
                return render(request, 'equipe/criar_equipe.html')
            
            equipe = Equipe(nome=nome, descricao=descricao, foto_perfil=foto_perfil, foto_capa=foto_capa)
            equipe.save()
            
            messages.success(request, "Equipe criada com sucesso!")
            return redirect('equipe_detalhes', id=equipe.id)
        return render(request, 'equipe/criar_equipe.html')  '''   
