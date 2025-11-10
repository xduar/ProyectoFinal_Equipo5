from django.db import models

# Create your models here.
from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo_electronico = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"


from django.conf import settings

class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=200)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Cita {self.fecha} {self.hora} - {self.paciente}"


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario
