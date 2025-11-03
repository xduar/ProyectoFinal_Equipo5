from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from clinica.models import Cita

class Command(BaseCommand):
    help = 'Configura los grupos, permisos y superusuarios iniciales del sistema'

    def handle(self, *args, **options):
        # Crear grupo para usuarios normales
        grupo_pacientes, created = Group.objects.get_or_create(name='Pacientes')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Pacientes" creado'))
        
        # Obtener los permisos necesarios para las citas
        content_type = ContentType.objects.get_for_model(Cita)
        permiso_crear_cita = Permission.objects.get(
            codename='add_cita',
            content_type=content_type,
        )
        permiso_ver_cita = Permission.objects.get(
            codename='view_cita',
            content_type=content_type,
        )
        
        # Asignar permisos al grupo de pacientes
        grupo_pacientes.permissions.add(permiso_crear_cita)
        grupo_pacientes.permissions.add(permiso_ver_cita)
        self.stdout.write(self.style.SUCCESS('Permisos asignados al grupo "Pacientes"'))
        
        # Crear superusuarios
        superusers = [
            {'username': 'admin1', 'email': 'admin1@clinica.com'},
            {'username': 'admin2', 'email': 'admin2@clinica.com'},
            {'username': 'admin3', 'email': 'admin3@clinica.com'},
        ]
        
        for admin in superusers:
            if not User.objects.filter(username=admin['username']).exists():
                User.objects.create_superuser(
                    username=admin['username'],
                    email=admin['email'],
                    password='Admin123!'  # Cambiar estas contraseñas inmediatamente después de la creación
                )
                self.stdout.write(
                    self.style.SUCCESS(f'Superusuario "{admin["username"]}" creado')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Superusuario "{admin["username"]}" ya existe')
                )