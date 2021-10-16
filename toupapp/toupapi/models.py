from django.db import models
from django.db.models.deletion import CASCADE

#Usuario del programa, que a su vez puede ser un trabajador o emprendedor
class usuario(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_username = models.CharField(max_length=50)
    usr_mail = models.CharField(max_length=150)
    usr_pass = models.CharField(max_length=150)
    usr_nombre = models.CharField(max_length=50)
    usr_apellidoPaterno = models.CharField(max_length=50)
    usr_apellidoMaterno = models.CharField(max_length=50)
    def __str__(self): #Para que cuando se busque tal modelo o se obtenga información de él, retorne lo indicado
        return "El id del usuario es: " + str(self.usr_id) + " y su nombre es: " + self.usr_username

#Tema de la startup, de que trata el proyecto o algo relacionado a él
class tema(models.Model):
    tem_id = models.AutoField(primary_key=True)
    tem_nombre = models.CharField(max_length=100)
    tem_desc = models.CharField(max_length=300)
    def __str__(self):
        return "El id del tema es: " + str(self.tem_id) + " y su nombre es: " + self.tem_nombre

#Contrato que se le "da" a los trabajadores para cumplir con lo establecido por la startup
class contrato(models.Model):
    cont_id = models.AutoField(primary_key=True)
    cont_tem_id = models.ForeignKey(tema, on_delete=CASCADE)
    def __str__(self):
        return "El id del contrato es: " + str(self.cont_id)


#Cargo que tendrá el trabajador de la startup
class cargo(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_nombre = models.CharField(max_length=100)
    car_desc = models.CharField(max_length=150)
    def __str__(self):
        return "El id del cargo es:" + str(self.car_id) + " y su nombre es: " + self.car_nombre

#trabajador del proyecto de startup del emprendedor
class trabajador(models.Model):
    tra_id = models.AutoField(primary_key=True)
    tra_usr_id = models.ForeignKey(usuario, on_delete=CASCADE)
    tra_car_id = models.ForeignKey(cargo, on_delete=CASCADE)
    tra_cont_id = models.ForeignKey(contrato, on_delete=CASCADE)
    def __str__(self):
        return "El id del trabajador es: " + str(self.tra_id)

#Uusuario que emprende el proyecto, y busca trabajadores bajo un contrato establecido por él y por la aplicación
class emprendedor(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_usr_id = models.ForeignKey(usuario, on_delete=CASCADE)
    def __str__(self):
        return "El id del emprendedor es: " + str(self.emp_id)

#Lo que crea el emprendedor para emprender
class proyecto(models.Model):
    pro_id = models.AutoField(primary_key=True)
    pro_nombre = models.CharField(max_length=150)
    pro_tem_id = models.ForeignKey(tema, on_delete=CASCADE)
    def __str__(self):
        return "El id del proyecto es: " + str(self.pro_id)