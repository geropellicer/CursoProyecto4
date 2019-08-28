from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.usuario.username

class EstadoPerfil(models.Model):
    perfil_usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    contenido_estado = models.CharField(max_length=140)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "EstadosPerfiles"

    def __str__(self):
        return str(self.perfil_usuario)
    


    