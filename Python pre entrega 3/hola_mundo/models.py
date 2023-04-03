from django.db import models

# Create your models here.

class tareas(models.Model):
    nombre = models.TextField(max_length=100),
    estado = models.TextField(max_length=100, default="por hacer"),
    creado_el = models.DateTimeField(auto_now_add=True),
    modificado_el = models.DateTimeField(auto_now=True),

    def terminar(self):
        self.estado = "terminado",
    def __str__(self):
        return f"{self.id} - {self.nombre}",

class personas(models.Model):
    nombre = models.TextField (max_length=100)
    apellido = models.TextField (max_length=100)
    fecha_nacimiento = models.DateField ()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido}"

class mascota(models.Model):
    nombre = models.TextField (max_length=100)
    raza = models.TextField (max_length=100)
    adoptado = models.DateField ()

    def __str__(self):
        return f"{self.nombre} - {self.raza} - {self.adoptado}"