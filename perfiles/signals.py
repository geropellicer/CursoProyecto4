from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from perfiles.models import Perfil, EstadoPerfil

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    print("Creado: ", created)
    if created:
        Perfil.objects.create(usuario=instance)