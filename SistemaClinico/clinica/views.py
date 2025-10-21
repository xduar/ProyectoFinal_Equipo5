from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.db import models as dj_models

from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm


def inicio(request):
    return render(request, 'clinica/inicio.html')


class PacienteListView(generic.ListView):
    model = Paciente
    template_name = 'clinica/paciente_list.html'
    context_object_name = 'pacientes'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().order_by('apellido', 'nombre')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(dj_models.Q(nombre__icontains=q) | dj_models.Q(apellido__icontains=q) | dj_models.Q(correo_electronico__icontains=q))
        return qs


class PacienteCreateView(generic.CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente_form.html'
    success_url = reverse_lazy('clinica:paciente_list')


class PacienteUpdateView(generic.UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente_form.html'
    success_url = reverse_lazy('clinica:paciente_list')


class PacienteDeleteView(generic.DeleteView):
    model = Paciente
    template_name = 'clinica/paciente_confirm_delete.html'
    success_url = reverse_lazy('clinica:paciente_list')


class PacienteDetailView(generic.DetailView):
    model = Paciente
    template_name = 'clinica/paciente_detail.html'


# Medico CRUD
class MedicoListView(generic.ListView):
    model = Medico
    template_name = 'clinica/medico_list.html'
    context_object_name = 'medicos'


class MedicoCreateView(generic.CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/medico_form.html'
    success_url = reverse_lazy('clinica:medico_list')


class MedicoUpdateView(generic.UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/medico_form.html'
    success_url = reverse_lazy('clinica:medico_list')


class MedicoDeleteView(generic.DeleteView):
    model = Medico
    template_name = 'clinica/medico_confirm_delete.html'
    success_url = reverse_lazy('clinica:medico_list')


class MedicoDetailView(generic.DetailView):
    model = Medico
    template_name = 'clinica/medico_detail.html'


# Cita CRUD
class CitaListView(generic.ListView):
    model = Cita
    template_name = 'clinica/cita_list.html'
    context_object_name = 'citas'
    
    def get_queryset(self):
        return super().get_queryset().order_by('fecha', 'hora')


class CitaCreateView(generic.CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'clinica/cita_form.html'
    success_url = reverse_lazy('clinica:cita_list')


class CitaUpdateView(generic.UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'clinica/cita_form.html'
    success_url = reverse_lazy('clinica:cita_list')


class CitaDeleteView(generic.DeleteView):
    model = Cita
    template_name = 'clinica/cita_confirm_delete.html'
    success_url = reverse_lazy('clinica:cita_list')


class CitaDetailView(generic.DetailView):
    model = Cita
    template_name = 'clinica/cita_detail.html'

def cita_completar(request, pk):
    if request.method == 'POST':
        cita = get_object_or_404(Cita, pk=pk)
        cita.delete()
        return redirect('clinica:cita_list')
