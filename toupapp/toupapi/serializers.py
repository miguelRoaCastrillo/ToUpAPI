from rest_framework import serializers
from toupapi.models import usuario, tema, contrato, cargo, trabajador, emprendedor, proyecto


class UsuarioSerializer(serializers.Serializer):
    usr_id = serializers.IntegerField(read_only=True)
    usr_username = serializers.CharField(required=True, allow_blank=False, max_length=50)
    usr_mail = serializers.CharField(required=True, allow_blank=False, max_length=150)
    usr_pass = serializers.CharField(required=True, allow_blank=False, max_length=150)
    usr_nombre = serializers.CharField(required=True, allow_blank=False, max_length=50)
    usr_apellidoPaterno = serializers.CharField(required=True, allow_blank=False, max_length=50)
    usr_apellidoMaterno = serializers.CharField(required=True, allow_blank=False, max_length=50)

    def create(self, validated_data):
        return usuario.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.usr_id = validated_data.get("usr_id", instance.usr_id)
        instance.usr_username = validated_data.get("usr_username", instance.usr_username)
        instance.usr_mail = validated_data.get("usr_mail", instance.usr_mail)
        instance.usr_pass = validated_data.get("usr_pass", instance.usr_pass)
        instance.usr_nombre = validated_data.get("usr_nombre", instance.usr_nombre)
        instance.usr_apellidoPaterno = validated_data.get("usr_apellidoPaterno", instance.usr_apellidoPaterno)
        instance.usr_apellidoMaterno = validated_data.get("usr_apellidoMaterno", instance.usr_apellidoMaterno)

        instance.save()
        return instance

class TemaSerializer(serializers.Serializer):
    tem_id = serializers.IntegerField(read_only=True)
    tem_nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    tem_desc = serializers.CharField(required=True, allow_blank=False, max_length=300)

    def create(self, validated_data):
        return tema.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tem_id = validated_data.get("tem_id", instance.tem_id)
        instance.tem_nombre = validated_data.get("tem_nombre", instance.tem_nombre)
        instance.tem_desc = validated_data.get("tem_desc", instance.tem_desc)        

        instance.save()
        return instance

class ContratoSerializer(serializers.Serializer):
    cont_id = serializers.IntegerField(read_only=True)
    cont_tem_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return contrato.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cont_id = validated_data.get("cont_id", instance.cont_id)
        instance.cont_tem_id = validated_data.get("cont_tem_id", instance.cont_tem_id)

        instance.save()
        return instance

class CargoSerializer(serializers.Serializer):
    car_id = serializers.IntegerField(read_only=True)
    car_nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    car_desc = serializers.CharField(required=True, allow_blank=False, max_length=150)

    def create(self, validated_data):
        return cargo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.car_id = validated_data.get("car_id", instance.car_id)
        instance.car_nombre = validated_data.get("car_nombre", instance.car_nombre)
        instance.car_desc = validated_data.get("car_desc", instance.car_desc)

        instance.save()
        return instance

class TrabajadorSerializer(serializers.Serializer):
    tra_id = serializers.IntegerField(read_only=True)
    tra_usr_id = serializers.IntegerField(read_only=True)
    tra_car_id = serializers.IntegerField(read_only=True)
    tra_cont_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return trabajador.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tra_id = validated_data.get("tra_id", instance.tra_id)
        instance.tra_usr_id = validated_data.get("tra_usr_id", instance.tra_usr_id)
        instance.tra_car_id = validated_data.get("tra_car_id", instance.tra_car_id)
        instance.tra_cont_id = validated_data.get("tra_cont_id", instance.tra_cont_id)
        
        instance.save()
        return instance

class EmprendedorSerializer(serializers.Serializer):
    emp_id = serializers.IntegerField(read_only=True)
    emp_usr_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return emprendedor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.emp_id = validated_data.get("emp_id", instance.emp_id)
        instance.emp_usr_id = validated_data.get("emp_usr_id", instance.emp_usr_id)

        instance.save()
        return instance

class ProyectoSerializer(serializers.Serializer):
    pro_id = serializers.IntegerField(read_only=True)
    pro_nombre = serializers.CharField(required=True, allow_blank=False, max_length=150)
    pro_tem_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return proyecto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pro_id = validated_data.get("pro_id", instance.pro_id)
        instance.pro_nombre = validated_data.get("pro_nombre", instance.pro_nombre)
        instance.pro_tem_id = validated_data.get("pro_tem_id", instance.pro_tem_id)

        instance.save()
        return instance

