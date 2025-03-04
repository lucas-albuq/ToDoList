import uuid
from django.db import models
from tarefas.models import Equipe, Categoria, Usuario

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
    ]
    PRIORIDADE_CHOICES = [
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=200)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pendente')
    prioridade = models.SmallIntegerField(null=True, choices=PRIORIDADE_CHOICES, blank=True) 
    prazo = models.DateField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    data_conclusao = models.DateField(null=True, blank=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

class Responsavel(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'tarefa')

class TarefaCategoria(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tarefa', 'categoria')
