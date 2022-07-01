from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.api.viewsets import UsuariosGet, UsuariosPost, UsuariosDetails
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
   # path('token/', TokenObtainPairView.as_view()),
   # path('token/refresh/', TokenRefreshView.as_view()),
    path('usuarios/', UsuariosGet.as_view()),
    path('usuarioscreate/', UsuariosPost.as_view()),
    path('usuarios/<int:id>/', UsuariosDetails.as_view()),
   # path('api-auth/', include('rest_framework.urls')),
]
