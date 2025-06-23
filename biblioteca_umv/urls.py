from django.urls import path, include
from django.contrib import admin
from usuarios.views import iniciar_sesion  # 👈 Importamos la vista de login

urlpatterns = [
    path('', iniciar_sesion, name='index'),  # 👈 Ahora la página principal es el login
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
]