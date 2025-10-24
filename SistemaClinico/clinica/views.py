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
    template_name = 'clinica/paciente.html'
    context_object_name = 'pacientes'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().order_by('apellido', 'nombre')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(dj_models.Q(nombre__icontains=q) | dj_models.Q(apellido__icontains=q) | dj_models.Q(correo_electronico__icontains=q))
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'list'
        return ctx


class PacienteCreateView(generic.CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente.html'
    success_url = reverse_lazy('clinica:paciente_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class PacienteUpdateView(generic.UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente.html'
    success_url = reverse_lazy('clinica:paciente_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class PacienteDeleteView(generic.DeleteView):
    model = Paciente
    template_name = 'clinica/paciente.html'
    success_url = reverse_lazy('clinica:paciente_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'confirm_delete'
        return ctx


class PacienteDetailView(generic.DetailView):
    model = Paciente
    template_name = 'clinica/paciente.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'detail'
        return ctx


# Medico CRUD
class MedicoListView(generic.ListView):
    model = Medico
    template_name = 'clinica/medico.html'
    context_object_name = 'medicos'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'list'
        return ctx


class MedicoCreateView(generic.CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/medico.html'
    success_url = reverse_lazy('clinica:medico_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class MedicoUpdateView(generic.UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/medico.html'
    success_url = reverse_lazy('clinica:medico_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class MedicoDeleteView(generic.DeleteView):
    model = Medico
    template_name = 'clinica/medico.html'
    success_url = reverse_lazy('clinica:medico_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'confirm_delete'
        return ctx


class MedicoDetailView(generic.DetailView):
    model = Medico
    template_name = 'clinica/medico.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'detail'
        return ctx


# Cita CRUD
class CitaListView(generic.ListView):
    model = Cita
    template_name = 'clinica/cita.html'
    context_object_name = 'citas'
    
    def get_queryset(self):
        return super().get_queryset().order_by('fecha', 'hora')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'list'
        return ctx


class CitaCreateView(generic.CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'clinica/cita.html'
    success_url = reverse_lazy('clinica:cita_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class CitaUpdateView(generic.UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'clinica/cita.html'
    success_url = reverse_lazy('clinica:cita_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class CitaDeleteView(generic.DeleteView):
    model = Cita
    template_name = 'clinica/cita.html'
    success_url = reverse_lazy('clinica:cita_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'confirm_delete'
        return ctx


class CitaDetailView(generic.DetailView):
    model = Cita
    template_name = 'clinica/cita.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'detail'
        return ctx

def cita_completar(request, pk):
    if request.method == 'POST':
        cita = get_object_or_404(Cita, pk=pk)
        cita.delete()
        return redirect('clinica:cita_list')
