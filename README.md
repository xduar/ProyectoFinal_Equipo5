# ProyectoFinal_Equipo5
### intregrantes 
- Amos Jeremias Leon Menjivar
- Brayan Josue Martinez Ardon
- Eduardo Enmanuel Menjivar Calderon
- Kenia Arely Monge Ruiz
- Kenia Lisbeht Hernandez Oliva
- Oscar Jonatan Vasquez Rivera
### Usuario de Githud
Usuario de Amos Leon: AmosLeon

Usuario de Brayan Martinez: brayanjosuemartinez41-wq

Usuario de Eduardo Menjivar: xduar

Usuario de Kenia Monge: arelyruiz488-png

Usuario de  Lisbeht Hernandez: lishernandez920-maker

Usuario de Jonatan Vasquez: OscarJonatanVasquezRivera

## Semana 3 – Implementación del CRUD en Django.

Con base en la guía anterior, se trabajó en el diseño y mejora de las vistas dentro del entorno web, enfocándose en la funcionalidad y la experiencia del usuario.

#### Pacientes
Se implementó un buscador que permite localizar pacientes por **nombre**, **apellido** o **correo electrónico**.  
Además, se añadió un **botón de “Nuevo Paciente”** para registrar nuevos pacientes en caso de que no estén en el sistema.  
También se incluyeron **acciones de edición y eliminación** para gestionar los registros existentes.

#### Médicos
Se desarrolló una vista para **registrar nuevos médicos** y **visualizar los ya existentes**.  
Cada registro cuenta con **botones de acción** que permiten **editar** o **eliminar** la información del médico.

#### Citas
Se agregó un **botón para crear nuevas citas**, permitiendo asignar a cada paciente un médico, junto con la **fecha**, **hora** y **motivo** de la cita.  
En la lista de citas, se incorporaron **acciones para ver, editar, marcar como realizada o eliminar** cada cita.

## Semana 4 – Autenticación de Usuarios y Diseño con Bootstrap

#### Sistema de Usuarios y Permisos
- Implementación de *sistema de autenticación* usando el modelo de usuario por defecto de Django
- Separación de roles entre *administradores* y *usuarios normales*
- Los superusuarios tienen acceso completo a todas las funcionalidades
- Los usuarios normales solo pueden gestionar citas

#### Mejoras en la Interfaz de Usuario
- Rediseño de la navegación para mostrar solo las opciones permitidas según el rol del usuario
- Mejora en los diálogos de confirmación usando modales de Bootstrap
- Nueva interfaz para confirmar citas realizadas con vista detallada de la información
- Diseño consistente en todas las confirmaciones (eliminar, completar citas)

#### Seguridad
- Protección de rutas sensibles con AdminRequiredMixin
- Todas las operaciones requieren autenticación (@login_required)
- Validación de permisos en el backend para prevenir accesos no autorizados
