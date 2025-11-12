from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from clinica.models import Cita, Paciente, Medico
import os

class Command(BaseCommand):
    help = 'Configura los grupos, permisos y superusuarios iniciales del sistema'

    def handle(self, *args, **options):
        # ========== CREAR GRUPOS ==========
        
        # Grupo Doctor: Solo Ver y Marcar como Realizada
        grupo_doctor, created = Group.objects.get_or_create(name='Doctor')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Doctor" creado'))
        
        # Grupo Secretaria: Acceso completo
        grupo_secretaria, created = Group.objects.get_or_create(name='Secretaria')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Secretaria" creado'))
        
        # Grupo Administrador: Control total
        grupo_admin, created = Group.objects.get_or_create(name='Administrador')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Administrador" creado'))
        
        # Grupo Usuario Registrado: Solo agregar pacientes
        grupo_usuario, created = Group.objects.get_or_create(name='Usuario Registrado')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Usuario Registrado" creado'))
        
        # ========== OBTENER PERMISOS ==========
        
        # Permisos de Cita
        cita_ct = ContentType.objects.get_for_model(Cita)
        cita_view = Permission.objects.get(codename='view_cita', content_type=cita_ct)
        cita_add = Permission.objects.get(codename='add_cita', content_type=cita_ct)
        cita_change = Permission.objects.get(codename='change_cita', content_type=cita_ct)
        cita_delete = Permission.objects.get(codename='delete_cita', content_type=cita_ct)
        
        # Permisos de Paciente
        paciente_ct = ContentType.objects.get_for_model(Paciente)
        paciente_view = Permission.objects.get(codename='view_paciente', content_type=paciente_ct)
        paciente_add = Permission.objects.get(codename='add_paciente', content_type=paciente_ct)
        paciente_change = Permission.objects.get(codename='change_paciente', content_type=paciente_ct)
        paciente_delete = Permission.objects.get(codename='delete_paciente', content_type=paciente_ct)
        
        # Permisos de Médico
        medico_ct = ContentType.objects.get_for_model(Medico)
        medico_view = Permission.objects.get(codename='view_medico', content_type=medico_ct)
        medico_add = Permission.objects.get(codename='add_medico', content_type=medico_ct)
        medico_change = Permission.objects.get(codename='change_medico', content_type=medico_ct)
        medico_delete = Permission.objects.get(codename='delete_medico', content_type=medico_ct)
        
        # ========== ASIGNAR PERMISOS A GRUPOS ==========
        
        # Doctor: Solo ver y marcar como realizada (view citas)
        grupo_doctor.permissions.set([cita_view])
        self.stdout.write(self.style.SUCCESS('Permisos asignados al grupo "Doctor"'))
        
        # Secretaria: Acceso completo
        grupo_secretaria.permissions.set([
            cita_view, cita_add, cita_change, cita_delete,
            paciente_view, paciente_add, paciente_change, paciente_delete,
            medico_view, medico_add, medico_change, medico_delete
        ])
        self.stdout.write(self.style.SUCCESS('Permisos asignados al grupo "Secretaria"'))
        
        # Administrador: Acceso completo (igual que Secretaria)
        grupo_admin.permissions.set([
            cita_view, cita_add, cita_change, cita_delete,
            paciente_view, paciente_add, paciente_change, paciente_delete,
            medico_view, medico_add, medico_change, medico_delete
        ])
        self.stdout.write(self.style.SUCCESS('Permisos asignados al grupo "Administrador"'))
        
        # Usuario Registrado: Solo agregar pacientes
        grupo_usuario.permissions.set([paciente_add, paciente_view])
        self.stdout.write(self.style.SUCCESS('Permisos asignados al grupo "Usuario Registrado"'))
        
        # ========== CREAR SUPERUSUARIOS Y ASIGNARLOS A GRUPOS ==========
        
        superusers = [
            {'username': 'Doctor', 'email': 'Doctor1@clinica.com', 'password': 'Doctor123!', 'group': 'Doctor'},
            {'username': 'Secretaria', 'email': 'Secretaria1@clinica.com', 'password': 'Secretaria123!', 'group': 'Secretaria'},
            {'username': 'admin3', 'email': 'admin3@clinica.com', 'password': 'Admin123!', 'group': 'Administrador'},
        ]
        
        for admin in superusers:
            user, created = User.objects.get_or_create(
                username=admin['username'],
                defaults={
                    'email': admin['email'],
                    'is_superuser': True,
                    'is_staff': True,
                }
            )
            if created:
                user.set_password(admin['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Superusuario "{admin["username"]}" creado'))
            else:
                self.stdout.write(self.style.WARNING(f'Superusuario "{admin["username"]}" ya existe'))
            
            # Asignar al grupo correspondiente
            group = Group.objects.get(name=admin['group'])
            user.groups.add(group)
        
        # Configurar la base de datos
        DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')
        self.stdout.write(self.style.SUCCESS(f'Conectado a la base de datos en {DATABASE_URL}'))