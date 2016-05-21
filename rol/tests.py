from django.test import TestCase

from rol.models import rol

# Create your tests here.


def crear_rol(nombre, descripcion):
	"""
	Funcion: Encargada de crear un rol para realizacion de pruebas
	"""
	return rol.objects.create(nombre=nombre, descripcion=descripcion)

class rolTest(TestCase):

	def test_creacion_rol(self):
		"""
		Se comprueba que el rol es creado exitosamente
		"""
		r = crear_rol("Administrador proyectoTest", "rol de prueba")
		r.save()
		tr = rol.objects.get(nombre="Administrador proyectoTest")
		self.assertEqual(tr.nombre, "Administrador proyectoTest")

	def test_eliminacion_rol(self):
		"""
		Se comprueba que la eliminacion del rol se realiza con exito
		"""
		r = crear_rol("Administrador proyectoTest", "rol de prueba")
		r.save()

		r = rol.objects.get(nombre="Administrador proyectoTest").delete()
		tr = rol.objects.all()

		self.assertEqual(tr.count(), 0)