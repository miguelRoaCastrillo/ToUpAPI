from rest_framework import serializers
from toupapi.models import usuario as Usuario, tema, contrato as Contrato, cargo as Cargo, trabajador as Trabajador, emprendedor as Emprendedor, proyecto as Proyecto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["usr_id", "usr_username", "usr_mail", "usr_mail", "usr_pass", "usr_nombre", "usr_apellidoPaterno", "usr_apellidoMaterno"]

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


class CargoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cargo
        fields = ("car_id", "car_nombre", "car_desc", "car_tema")

class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trabajador
        fields = ("tra_id", "tra_usr_id", "tra_car_id")

class TrabajadorByTemaSerializer(serializers.ModelSerializer):    

    tra_usr_nombre = serializers.CharField(source='tra_usr_id.usr_nombre')
    tra_usr_apellidoPaterno = serializers.CharField(source='tra_usr_id.usr_apellidoPaterno')
    tra_usr_apellidoMaterno = serializers.CharField(source='tra_usr_id.usr_apellidoMaterno')
    tra_usr_mail = serializers.CharField(source='tra_usr_id.usr_mail')
    tra_usr_usrname = serializers.CharField(source='tra_usr_id.usr_username')
    tra_car_nombre = serializers.CharField(source='tra_car_id.car_nombre')

    class Meta:
        model= Trabajador
        fields = (
            'tra_id'
            , 'tra_usr_nombre'
            , 'tra_usr_apellidoPaterno'
            , 'tra_usr_apellidoMaterno'
            , 'tra_usr_mail'
            , 'tra_usr_usrname'
            , 'tra_car_id'
            , 'tra_car_nombre'
        )

class EmprendedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emprendedor
        fields = ("emp_id", "emp_usr_id")

class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyecto
        fields = ("pro_id", "pro_nombre", "pro_tem_id", "pro_users", "pro_desc")
    
