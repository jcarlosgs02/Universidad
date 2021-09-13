from django.db import models

# Create your models here.


class Carrera(models.Model):
   codigo=models.CharField(max_length=3,primary_key=True)
   nombre=models.CharField(max_length=50)
   direccion=models.PositiveSmallIntegerField(default=5)

class Estudiante(models.Model):
   dni=models.CharField(max_length=8,primary_key=True)
   nombre=models.CharField(max_length=50)
   fechaNacimiento=models.DateField()
   sexos = [
   ('F','Femenino'),
   ('M','Masculino')
    ]
   sexo = models.CharField(max_length=1, choices=sexos, default='F')
   carrera=models.ForeignKey(Carrera,null=False,blank=False,on_delete=models.CASCADE)

class Curso(models.Model):
    codigo=models.CharField(max_length=6,primary_key=True)
    nombre=models.CharField(max_length=30)
    creditos=models.PositiveSmallIntegerField()
    docente=models.CharField(max_length=100)  

class Matricula(models.Model):
   id=models.AutoField(primary_key=True) 
   estudiante=models.ForeignKey(Estudiante,null=False,blank=False,on_delete=models.CASCADE)
   curso=models.ForeignKey(Curso,null=False,blank=False, on_delete=models.CASCADE)
   fechaMatricula = models.DateTimeField(auto_now_add=True)