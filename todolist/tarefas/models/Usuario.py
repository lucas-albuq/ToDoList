import uuid
from django.db import models
from .Equipe import Equipe
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, nome, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    google_id = models.CharField(max_length=100, blank=True, null=True)
    foto_perfil = models.ImageField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    def __str__(self):
        return f'{self.nome} - {self.email}'

class UsuarioEquipe(models.Model):
    CARGO_CHOICES = [
        (1, 'Proprietário'),
        (2, 'Administrador'),
        (3, 'Membro'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    cargo = models.IntegerField(choices=CARGO_CHOICES, default=3) 

    class Meta:
        unique_together = ('usuario', 'equipe')

    def __str__(self):
        return f"{self.usuario.email} - {dict(self.CARGO_CHOICES).get(self.cargo)} - {self.equipe.nome}"
