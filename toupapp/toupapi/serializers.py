from rest_framework import serializers
from toupapi.models import usuario, tema, contrato as Contrato, cargo, trabajador as Trabajador, emprendedor as Emprendedor, proyecto as Proyecto


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

class ContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contrato
        fields = ("cont_id", "cont_tem_id")


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

class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trabajador
        fields = ("tra_id", "tra_usr_id", "tra_car_id", "tra_cont_id")

class EmprendedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emprendedor
        fields = ("emp_id", "emp_usr_id")

class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyecto
        fields = ("pro_id", "pro_nombre", "pro_tem_id", "pro_users")

