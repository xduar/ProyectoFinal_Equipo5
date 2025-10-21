from django.contrib import admin
from .models import Paciente, Medico, Cita, Usuario


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'telefono', 'correo_electronico')


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'telefono')


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'hora', 'paciente', 'medico')


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('nombre_usuario',)
