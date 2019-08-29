from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from perfiles.models import Perfil, EstadoPerfil
from perfiles.api.serializers import PerfilSerializer, EstadoPerfilSerializer, AvatarPerfilSerializer
# from rest_framework.viewsets import ReadOnlyModelViewSet
from perfiles.api.permissions import EsPerfilPropioOrReadOnly, EsOwnerOrReadOnly
from rest_framework.filters import SearchFilter

# class ListaPerfiles(generics.ListAPIView):
#     queryset = Perfil.objects.all()
#     serializer_class = PerfilSerializer
#     permission_classes = [IsAuthenticated]

class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = AvatarPerfilSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.perfil
        return profile_object

class PerfilViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated, EsPerfilPropioOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['city']

class EstadoPerfilViewSet(ModelViewSet):
    serializer_class = EstadoPerfilSerializer
    permission_classes = [IsAuthenticated, EsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = EstadoPerfil.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(perfil_usuario__usuario__username=username)
        return queryset

    def perform_create(self, serializer):
        perfil_usuario = self.request.user.perfil
        serializer.save(perfil_usuario=perfil_usuario)
