from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.db import models as dj_models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout

from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm, RegistroUsuarioForm

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


def inicio(request):
    return render(request, 'clinica/inicio.html')


class PacienteListView(AdminRequiredMixin, LoginRequiredMixin, generic.ListView):
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


class PacienteCreateView(AdminRequiredMixin, LoginRequiredMixin, generic.CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente.html'
    success_url = reverse_lazy('clinica:paciente_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class PacienteUpdateView(AdminRequiredMixin, LoginRequiredMixin, generic.UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente.html'
    success_url = reverse_lazy('clinica:paciente_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class PacienteDeleteView(AdminRequiredMixin, LoginRequiredMixin, generic.DeleteView):
    model = Paciente
    template_name = 'clinica/paciente.html'
    success_url = reverse_lazy('clinica:paciente_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'confirm_delete'
        return ctx


class PacienteDetailView(AdminRequiredMixin, LoginRequiredMixin, generic.DetailView):
    model = Paciente
    template_name = 'clinica/paciente.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'detail'
        return ctx


# Medico CRUD
class MedicoListView(AdminRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = Medico
    template_name = 'clinica/medico.html'
    context_object_name = 'medicos'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'list'
        return ctx


class MedicoCreateView(AdminRequiredMixin, LoginRequiredMixin, generic.CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/medico.html'
    success_url = reverse_lazy('clinica:medico_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class MedicoUpdateView(AdminRequiredMixin, LoginRequiredMixin, generic.UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/medico.html'
    success_url = reverse_lazy('clinica:medico_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class MedicoDeleteView(AdminRequiredMixin, LoginRequiredMixin, generic.DeleteView):
    model = Medico
    template_name = 'clinica/medico.html'
    success_url = reverse_lazy('clinica:medico_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'confirm_delete'
        return ctx


class MedicoDetailView(AdminRequiredMixin, LoginRequiredMixin, generic.DetailView):
    model = Medico
    template_name = 'clinica/medico.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'detail'
        return ctx


# Cita CRUD
class CitaListView(LoginRequiredMixin, generic.ListView):
    model = Cita
    template_name = 'clinica/cita.html'
    context_object_name = 'citas'
    
    def get_queryset(self):
        # Si es superusuario, puede ver todas las citas
        if self.request.user.is_superuser:
            return super().get_queryset().order_by('fecha', 'hora')
        # Si es usuario normal, solo ve sus citas
        return super().get_queryset().filter(usuario=self.request.user).order_by('fecha', 'hora')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'list'
        return ctx


class CitaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'clinica/cita.html'
    success_url = reverse_lazy('clinica:cita_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class CitaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'clinica/cita.html'
    success_url = reverse_lazy('clinica:cita_list')

    def get_queryset(self):
        # Si es superusuario, puede editar todas las citas
        if self.request.user.is_superuser:
            return super().get_queryset()
        # Si es usuario normal, solo puede editar sus citas
        return super().get_queryset().filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'form'
        return ctx


class CitaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cita
    template_name = 'clinica/cita.html'
    success_url = reverse_lazy('clinica:cita_list')

    def get_queryset(self):
        # Si es superusuario, puede eliminar todas las citas
        if self.request.user.is_superuser:
            return super().get_queryset()
        # Si es usuario normal, solo puede eliminar sus citas
        return super().get_queryset().filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'confirm_delete'
        return ctx


class CitaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cita
    template_name = 'clinica/cita.html'

    def get_queryset(self):
        # Si es superusuario, puede ver todas las citas
        if self.request.user.is_superuser:
            return super().get_queryset()
        # Si es usuario normal, solo puede ver sus citas
        return super().get_queryset().filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = 'detail'
        return ctx


@login_required
def cita_completar(request, pk):
    if request.method == 'POST':
        cita = get_object_or_404(Cita, pk=pk)
        cita.delete()
        return redirect('clinica:cita_list')
    return redirect('clinica:cita_list')


@login_required
def dashboard(request):
    return render(request, 'clinica/dashboard.html')


class RegistroView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'clinica/register.html'
    success_url = reverse_lazy('clinica:inicio')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


def logout_confirm(request):
    """Mostrar confirmación en GET; hacer logout y redirigir en POST."""
    if request.method == 'POST':
        auth_logout(request)
        return redirect('clinica:inicio')
    return render(request, 'clinica/logout_confirm.html')


