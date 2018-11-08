from django.db import models

# Create your models here.

class Region(models.Model):
    idregion=models.IntegerField(primary_key=True,verbose_name="idregion")
    descripcion=models.TextField()

    def __str__(self):
        return self.descripcion
class Ciudad(models.Model):
    idciudad=models.IntegerField(primary_key=True,verbose_name="idciudad")
    descripcion=models.TextField()
    idregion=models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Comuna(models.Model):
    idcomuna=models.IntegerField(primary_key=True,verbose_name="idcomuna")
    descripcion=models.TextField()
    idciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)

class TipoUsuario(models.Model):
    idtipo=models.IntegerField(primary_key=True,verbose_name="idtipo")
    descripcion=models.TextField()

    def __str__(self):
        return self.descripcion


class Estado(models.Model):
    idestado=models.IntegerField(primary_key=True)
    descripcion=models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Mascota(models.Model):
    nombre=models.CharField(max_length=50,primary_key=True,verbose_name="nombre")
    raza=models.CharField(max_length=50)
    descripcion=models.TextField()
    estado=models.CharField(max_length=45)
    foto=models.FileField()

    def __str__(self):
        return self.nombre


class Registro(models.Model):
    rut=models.CharField(max_length=40,primary_key=True)
    nombre=models.CharField(max_length=45)
    apellido=models.CharField(max_length=45)
    ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    region=models.ForeignKey(Region,on_delete=models.CASCADE)
    comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE)
    correo=models.CharField(max_length=45)

    def __str__(self):
        return self.rut

        