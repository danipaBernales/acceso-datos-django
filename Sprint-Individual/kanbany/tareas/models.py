from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} (Nivel {self.nivel})"

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada')
    ])
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length=20, choices=[
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja')
    ])
    
    def __str__(self):
        return self.titulo
