import uuid
from django.db import models
from .Equipe import Equipe

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255) 
    foto_perfil = models.CharField(max_length=300, blank=True, null=True)

class UsuarioEquipe(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    cargo = models.IntegerField()  # Poderia ser um ENUM

    class Meta:
        unique_together = ('usuario', 'equipe')