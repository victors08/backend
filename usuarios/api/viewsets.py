from rest_framework import viewsets
from usuarios.api import serializers
from usuarios import models
from rest_framework.permissions import IsAuthenticated

class UsuariosViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  serializer_class = serializers.UsuariosSerializer
  queryset = models.Usuarios.objects.all()