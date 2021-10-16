from django.contrib import admin
from django.urls import path, include
from toupapi import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', views.UsuariosView)
urlpatterns = [
    #path('usuarios/', views.usuarios_list),
    #path('usuarios/<int:pk>', views.usuario_detail)
    path('api/', include(router.urls))    
]
