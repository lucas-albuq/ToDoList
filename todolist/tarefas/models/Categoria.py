import uuid
from django.db import models
from tarefas.models import Equipe

class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=7)  # HEX "#RRGGBB"
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)