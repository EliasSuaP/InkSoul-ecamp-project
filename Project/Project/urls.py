"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web.views import index, mitologicos, reserva, animales, kit, gracias, maories, tatuadores

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path('', index, name='Bienvenida'), 
    # Forms   
    path('reserva/', reserva, name='Reserva'),
    path('gracias/', gracias, name='Gracias'),
    # Kit venta
    path('kit/', kit, name='Kit'),
    # tatuadores
    path('tatuadores/', tatuadores, name='Tatuadores'),
    # Galerias de imágenes
    path('animales/', animales, name='Animales'),
    path('maories/', maories, name='Maories'),
    path('mitologicos/', mitologicos, name='Mitologicos'), 
    # Login 
    path('accounts/', include('django.contrib.auth.urls'))   
]
