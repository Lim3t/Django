from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

class Cliente(models.Model):
    nombre = models.CharField(max_length=6,verbose_name='Nombre Cliente')
    apellido = models.CharField(max_length=20, verbose_name='Apellido Cliente')
    direccion = models.CharField(max_length=20,null=True,blank=True, verbose_name='Direccion Cliente')
    correo = models.CharField(max_length=20,null=True,blank=True, verbose_name='Correo Cliente')
    comuna = models.CharField(max_length=20,null=True,blank=True, verbose_name='Comuna Cliente')
    edad = models.CharField(max_length=20,null=True,blank=True, verbose_name='Edad Cliente')
    comentario = models.CharField(max_length=200,null=True,blank=True, verbose_name='Comentario Cliente')
    Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


