from django.db import models

#Usuario del programa, que a su vez puede ser un trabajador o emprendedor
class usuario(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_username = models.CharField(max_length=50)
    usr_mail = models.CharField(max_length=150)
    usr_pass = models.CharField(max_length=150)
    usr_nombre = models.CharField(max_length=50)
    usr_apellidoPaterno = models.CharField(max_length=50)
    usr_apellidoMaterno = models.CharField(max_length=50)

    def __str__(self): 
        return "id_usuario: " + str(self.usr_id) + ", nombre: " + self.usr_nombre

    def __unicode__(self):
        return self.usr_id

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
    cont_tem_id = models.ForeignKey(tema, on_delete=models.CASCADE)
    def __str__(self):
        return "El id del contrato es: " + str(self.cont_id)


#Cargo que tendrá el trabajador de la startup
class cargo(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_nombre = models.CharField(max_length=100)
    car_desc = models.CharField(max_length=150)
    car_tema = models.ManyToManyField(tema)
    
    def __str__(self):
        return "El id del cargo es:" + str(self.car_id) + " y su nombre es: " + self.car_nombre

#trabajador del proyecto de startup del emprendedor
class trabajador(models.Model):
    tra_id = models.AutoField(primary_key=True)
    tra_usr_id = models.ForeignKey(usuario, on_delete=models.CASCADE)
    tra_car_id = models.ForeignKey(cargo, on_delete=models.CASCADE)    

    def __str__(self):
        return "id_trabajador: " + str(self.tra_id) + ", tra_usr_id: " + str(self.tra_usr_id)

#Uusuario que emprende el proyecto, y busca trabajadores bajo un contrato establecido por él y por la aplicación
class emprendedor(models.Model):

    emp_id = models.AutoField(primary_key=True)
    emp_usr_id = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        return "Emprendedor: " + str(self.emp_id) + ", usr_id: " + self.emp_usr_id

#Lo que crea el emprendedor para emprender
class proyecto(models.Model):

    pro_id = models.AutoField(primary_key=True)
    pro_nombre = models.CharField(max_length=150)
    pro_tem_id = models.ForeignKey(tema, on_delete=models.CASCADE)
    pro_users = models.ManyToManyField(usuario)
    pro_desc = models.CharField(max_length=300, null=True)

    def __str__(self):
        return str(self.pro_id) + ": " + self.pro_nombre