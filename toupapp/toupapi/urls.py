from django.contrib import admin
from django.urls import path
from toupapi import views

urlpatterns = [
    path('usuarios/', views.usuarios_list),
    path('usuarios/<int:pk>', views.usuario_detail)
    #path('admin/', admin.site.urls),
]
