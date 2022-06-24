from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.api import viewsets as usuariosviewsets

router = routers.DefaultRouter()
router.register(r'usuarios', usuariosviewsets.UsuariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
