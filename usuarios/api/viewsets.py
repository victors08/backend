import email
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from rest_framework import generics
from rest_framework import filters
# from rest_framework.permissions import IsAuthenticated

from usuarios import models
from .serializers import UsuariosSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend

import json


class UsuariosGet(APIView):
  def get(self, request):
    usuarios = models.Usuarios.objects.all()
    serializer = UsuariosSerializer(usuarios, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class UsuarioLogin(generics.ListAPIView):
  serializer_class = UsuariosSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['email']
  

class UsuariosPost(APIView):
  def post(self, request):
    serializer = UsuariosSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuariosGetEspecifico(APIView):
 def get(self, request, id):
  usuario = get_object_or_404(models.Usuarios.objects.all(), id=id)
  serializer = UsuariosSerializer(usuario)
  return Response(serializer.data, status = status.HTTP_200_OK)

class UsuariosPut(APIView):
  def put(self, request, id):
    usuario = get_object_or_404(models.Usuarios.objects.all(), id=id)
    serializer = UsuariosSerializer(usuario, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsuariosDelete(APIView):
  def get(self, request, id):
    usuario = get_object_or_404(models.Usuarios.objects.all(), id=id)
    usuario.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)