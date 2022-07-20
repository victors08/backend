from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.api.viewsets import UsuariosGet, UsuariosPost, UsuariosGetEspecifico, UsuariosPut, UsuariosDelete
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('usuarios/', UsuariosGet.as_view()),
    path('usuarios/create/', UsuariosPost.as_view()),
    path('usuarios/<int:id>/', UsuariosGetEspecifico.as_view()),
    path('usuarios/update/<int:id>/', UsuariosPut.as_view()),
    path('usuarios/delete/<int:id>/', UsuariosDelete.as_view()),
]
