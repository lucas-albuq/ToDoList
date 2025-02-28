import uuid
from django.db import models

class Equipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)