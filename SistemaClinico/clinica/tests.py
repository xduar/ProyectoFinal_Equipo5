from django.test import TestCase
from .models import Paciente
from .forms import PacienteForm


class PacienteModelTest(TestCase):
	def test_crear_paciente(self):
		p = Paciente.objects.create(nombre='Juan', apellido='Perez')
		self.assertEqual(str(p), 'Juan Perez')


class PacienteFormTest(TestCase):
	def test_telefono_invalido(self):
		form = PacienteForm(data={'nombre': 'Ana', 'apellido': 'Lopez', 'telefono': '12'})
		self.assertFalse(form.is_valid())
		self.assertIn('telefono', form.errors)
