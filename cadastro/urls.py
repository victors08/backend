from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.api.viewsets import UsuariosGet, UsuarioLogin, UsuariosPost, UsuariosGetEspecifico, UsuariosPut, UsuariosDelete
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('usuarios/', UsuariosGet.as_view()),
    path('login/<email>', UsuarioLogin.as_view()),
    path('usuarios/create/', UsuariosPost.as_view()),
    path('usuarios/<int:id>/', UsuariosGetEspecifico.as_view()),
    path('usuarios/update/<int:id>/', UsuariosPut.as_view()),
    path('usuarios/delete/<int:id>/', UsuariosDelete.as_view()),
]
