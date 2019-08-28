from rest_framework import serializers
from perfiles.models import Perfil, EstadoPerfil

class PerfilSerializer(serializers.ModelSerializer):
    
    usuario = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Perfil
        fields = "__all__"

class AvatarPerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = ('avatar',)

class  EstadoPerfilSerializer(serializers.ModelSerializer):
    perfil_usuario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = EstadoPerfil
        fields = "__all__"