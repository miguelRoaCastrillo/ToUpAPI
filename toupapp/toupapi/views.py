from re import S
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.parsers import JSONParser
from toupapi.models import usuario as Usuario, tema, contrato, cargo, trabajador, emprendedor, proyecto
from toupapi.serializers import UsuarioSerializer, TemaSerializer, ContratoSerializer, CargoSerializer, TrabajadorSerializer, EmprendedorSerializer, ProyectoSerializer

# Usuarios
class UsuariosView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

@csrf_exempt
def usuarios_list(request):
    if request.method == "GET":
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def usuario_detail(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = UsuarioSerializer(usuario)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        usuario.detele()
        return HttpResponse(status=204)
    
#Temas
class TemasView(viewsets.ModelViewSet):
    queryset = tema.objects.all()
    serializer_class = TemaSerializer

