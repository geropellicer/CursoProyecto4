# from django.urls import path
# from perfiles.api.views import ListaPerfiles

# urlpatterns = [
#     path('perfiles/', ListaPerfiles.as_view(), name='lista-perfiles')
# ]

# from django.urls import path
# from perfiles.api.views import PerfilViewSet

# lista_perfil = PerfilViewSet.as_view({"get": 'list'})
# detalles_perfil = PerfilViewSet.as_view({"get": 'retrieve'})    

# urlpatterns = [
#     path("perfiles/", lista_perfil, name="lista-perfil"),
#     path("perfiles/<int:pk>/", detalles_perfil, name="detalles-perfil")
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from perfiles.api.views import PerfilViewSet, EstadoPerfilViewSet, AvatarUpdateView

router = DefaultRouter()
router.register(r"perfiles", PerfilViewSet)
router.register(r"estados", EstadoPerfilViewSet, basename="estados")

urlpatterns = [
    path('', include(router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name="avatar-update")
]



