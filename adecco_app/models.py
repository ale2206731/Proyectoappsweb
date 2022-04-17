from django.db import models
import datetime

# Create your models here.
class Noticias (models.Model):
    encabezado = models.CharField(max_length=100, blank=False,null=False)
    descripcion = models.TextField(blank=False, null=False)
    
    autor = models.CharField(max_length=100,blank=False, null=False)
    fecha = models.DateField(default=datetime.date.today, blank=False,null=False)

    def __str__(self):
        return self.encabezado

class Comentarios(models.Model):
    nombre=models.CharField(max_length=150, blank=False, null=False)
    email=models.EmailField(max_length=150, blank=False, null=False)
    telefono= models.CharField(max_length=150, blank=False, null=False)
    comentario = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return self.nombre