from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.api import viewsets as usuariosviewsets

route = routers.DefaultRouter()
route.register(r'usuarios/', usuariosviewsets.UsuariosViewSet, basename="Usuários")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
