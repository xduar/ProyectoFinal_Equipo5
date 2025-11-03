from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Paciente

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Añadir el usuario al grupo de Pacientes
            grupo_pacientes = Group.objects.get_or_create(name='Pacientes')[0]
            user.groups.add(grupo_pacientes)
        return user


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'correo_electronico']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_telefono(self):
        t = self.cleaned_data.get('telefono')
        if t:
            digits = ''.join(ch for ch in t if ch.isdigit())
            if len(digits) < 7:
                raise forms.ValidationError('Número de teléfono demasiado corto.')
        return t


from .models import Medico, Cita


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_telefono(self):
        t = self.cleaned_data.get('telefono')
        if t:
            digits = ''.join(ch for ch in t if ch.isdigit())
            if len(digits) < 7:
                raise forms.ValidationError('Número de teléfono demasiado corto.')
        return t


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'hora', 'motivo', 'paciente', 'medico']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-select select2'}),
            'medico': forms.Select(attrs={'class': 'form-select select2'}),
        }