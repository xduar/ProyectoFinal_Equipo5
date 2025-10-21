from django.urls import path
from . import views

app_name = 'clinica'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pacientes/', views.PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/editar/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/', views.PacienteDeleteView.as_view(), name='paciente_delete'),
    path('pacientes/<int:pk>/', views.PacienteDetailView.as_view(), name='paciente_detail'),
    # Medico
    path('medicos/', views.MedicoListView.as_view(), name='medico_list'),
    path('medicos/nuevo/', views.MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/editar/', views.MedicoUpdateView.as_view(), name='medico_update'),
    path('medicos/<int:pk>/eliminar/', views.MedicoDeleteView.as_view(), name='medico_delete'),
    path('medicos/<int:pk>/', views.MedicoDetailView.as_view(), name='medico_detail'),
    # Cita
    path('citas/', views.CitaListView.as_view(), name='cita_list'),
    path('citas/nuevo/', views.CitaCreateView.as_view(), name='cita_create'),
    path('citas/<int:pk>/editar/', views.CitaUpdateView.as_view(), name='cita_update'),
    path('citas/<int:pk>/eliminar/', views.CitaDeleteView.as_view(), name='cita_delete'),
    path('citas/<int:pk>/', views.CitaDetailView.as_view(), name='cita_detail'),
    path('citas/<int:pk>/completar/', views.cita_completar, name='cita_completar'),
]
