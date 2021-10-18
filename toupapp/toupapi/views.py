from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.parsers import JSONParser
from toupapi.models import usuario as Usuario, tema as Tema, contrato as Contrato, cargo as Cargo, trabajador as Trabajador, emprendedor as Emprendedor, proyecto as Proyecto
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

#Usuario segun parámetros
class UsuariosByParamsView(viewsets.ModelViewSet):    
    serializer_class = UsuarioSerializer    

    #Busca por get
    def get_queryset(self):        
        username = self.request.query_params.get('username')
        print(username)
        if username is not None:
            queryset = Usuario.objects.filter(usr_username = username)
        return queryset


#Temas
class TemasView(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

@csrf_exempt
def temas_list(request):
    if request.method == "GET":
        temas = Tema.objects.all()
        serializer = TemaSerializer(temas, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TemaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errores, status=400)
    
def temas_detail(request, pk):
    try:
        tema = Tema.objects.get(pk=pk)
    except Tema.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = TemaSerializer(tema)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TemaSerializer(tema, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        tema.delete()
        return HttpResponse(status=204)

#Contratos
class ContratosView(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

@csrf_exempt
def contratos_list(request):
    if request.method == "GET":
        contratos = Contrato.objects.all()
        serializer = ContratoSerializer(contratos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ContratoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializers.errores, status=400)

def contrato_detail(request, pk):
    try:
        contrato = Contrato.objects.get(pk=pk)
    except Contrato.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = ContratoSerializer(contrato)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ContratoSerializer(contrato, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        contrato.delete()
        return HttpResponse(status=204)

#Cargos
class CargosView(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

@csrf_exempt
def cargos_list(request):
    if request.method == "GET":
        cargos = Cargo.objects.all()
        serializer = CargoSerializer(cargos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CargoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializers.errores, status=400)

def cargos_detail(request, pk):
    try:
        cargo = Cargo.objects.get(pk=pk)
    except Cargo.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = CargoSerializer(cargo)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CargoSerializer(cargo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        cargo.delete()
        return HttpResponse(status=204)
     
#Trabajadores
class TrabajadoresView(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer

@csrf_exempt
def trabajadores_list(request):
    if request.method == "GET":
        trabajadores = Trabajador.objects.all()
        serializer = TrabajadorSerializer(trabajadores, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TrabajadorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializers.errores, status=400)

def trabajadores_detail(request, pk):
    try:
        trabajador = Trabajador.objects.get(pk=pk)
    except Trabajador.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = TrabajadorSerializer(trabajador)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TrabajadorSerializer(trabajador, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        trabajador.delete()
        return HttpResponse(status=204)
     
#Para traer trabajadores segun los temas que se busquen
class TrabadoresByParamsView(viewsets.ModelViewSet):
    serializer_class = TrabajadorSerializer

    def get_queryset(self):
        temaparam = self.request.query_params.get('tema')
        print(temaparam)
        if temaparam is not None:            

            cargos = Cargo.objects.filter(car_tema = temaparam)
            trabajadores = Trabajador.objects.all()

            print(cargos)
            print(trabajadores)

            data = []

            for cargo in cargos:
                print(cargo.car_id)
                for trabajador in trabajadores:
                    print(trabajador.tra_car_id)
                    if trabajador.tra_car_id.car_id == cargo.car_id:
                        print("Los cargos coincidieron")
                        data.append(trabajador)      
                        

        return data
            
#Emprendedores
class EmprendedoresView(viewsets.ModelViewSet):
    queryset = Emprendedor.objects.all()
    serializer_class = EmprendedorSerializer
    
@csrf_exempt
def emprendedores_list(request):
    if request.method == "GET":
        emprendedores = Emprendedor.objects.all()
        serializer = EmprendedorSerializer(emprendedores, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = EmprendedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializers.errores, status=400)

def emprendedores_detail(request, pk):
    try:
        emprendedor = Emprendedor.objects.get(pk=pk)
    except Emprendedor.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = EmprendedorSerializer(emprendedor)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TrabajadorSerializer(emprendedor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        emprendedor.delete()
        return HttpResponse(status=204)


#Proyecto
class ProyectosView(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    
@csrf_exempt
def emprendedores_list(request):
    if request.method == "GET":
        proyectos = Emprendedor.objects.all()
        serializer = ProyectoSerializer(proyectos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProyectoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializers.errores, status=400)

def emprendedores_detail(request, pk):
    try:
        proyecto = Emprendedor.objects.get(pk=pk)
    except Emprendedor.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = ProyectoSerializer(proyecto)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TrabajadorSerializer(proyecto, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        proyecto.delete()
        return HttpResponse(status=204)