from django.contrib import admin
from django.urls import path, include
from toupapi import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', views.UsuariosView)
router.register('temas', views.TemasView)
router.register('contratos', views.ContratosView)
router.register('cargos', views.CargosView)
router.register('trabajadores', views.TrabajadoresView)
router.register('emprendedores', views.EmprendedoresView)
router.register('proyectos', views.ProyectosView)
router.register('usrByParams', views.UsuariosByParamsView, basename='Usuario') 
router.register('TrabadoresByParamsView', views.TrabadoresByParamsView, basename='Tema')


urlpatterns = [
    #path('usuarios/', views.usuarios_list),
    #path('usuarios/<int:pk>', views.usuario_detail)
    path('api/', include(router.urls)),
    path('prediccion/', views.predicionResults)
]
