
from django.test import TestCase


from actividad.models import actividad
from proyecto.models import proyecto
from flujo.models import flujo
from scrummer.models import Usuario
# Create your tests here.

def crear_usuario(nombre, apellido, nombreUsuario, contrasenha, direccion, correo, telefono, observacion, estado, roles):
	"""
	Funcion: Encargada de crear un usuario para la realizacion de pruebas
	"""
	return Usuario.objects.create(nombre='Juan', apellido='Valdez', nombreUsuario='usuario1',
								contrasenha='usu1', direccion='Pedro Getto 548',
								correo=4100100, telefono=45848565, observacion='Desarrollador de Django',
                                estado='activo',roles='desarrollador'
								)

def crear_proyecto(nombre, descripcion, fecha_creacion, complejidad_total, estado):
	"""
	Funcion: Encargada de crear un proyecto para realizacion de pruebas
	"""
	return proyecto.objects.create(nombre=nombre, descripcion=descripcion,
								 fechaInicio=fechaInicio,
								 fechaFin=fechaFin
								 )
def crear_flujo(nombre):
	"""
	Funcion: Encargada de crear un flujo para la realizacion de pruebas
	"""
	return flujo.objects.create(nombre=nombre, proyecto= proyecto)


def crear_actividad(nombre, orden,flujo):
	"""
	Funcion: Encargada de crear una actividad para realizacion de pruebas
	"""
	return actividad.objects.create(nombre=nombre, orden=orden,
								 flujo=flujo
								 )

class ActividadTest(TestCase):

	def test_creacion_actividad(self):
		"""
		Se comprueba que la actividad es creada exitosamente
		"""
		a = crear_actividad("actividadTest",1,"flujo de prueba")
		ta = actividad.objects.get(nombre="actividadTest")
		self.assertEqual(ta.nombre, "actividadTest")

	def test_eliminacion_actividad(self):
		"""
		Se comprueba que al eliminar la actividad, todos los flujos
		asociados al mismo tambien son eliminados
		"""
		p = crear_proyecto("proyectoTest", "Prueba de test.py", timezone.now(), timezone.now())
		p.save()
		f = crear_flujo("Flujo de prueba", "proyectoTest")
		f.proyecto = p
		f.save()
		actividad.objects.get(nombre="actividadTest").delete()
		ta = actividad.objects.all()
		f = flujo.objects.all()
		self.assertEqual(len(ta), 0)
		self.assertEqual(len(f), 0)

	def test_conexion(self):


		usuario = crear_usuario('admin', 'admin')
		usuario.save()
		a = crear_actividad("actividadTest",1, "Flujo de prueba")
		p.save()
		res = self.client.post('/login/',{'username':'admin','password':'admin'})
		tsession = self.client.session
		print 'data'
		print tsession
		print tsession['usuario']
		print res
		self.assertEqual(tsession['usuario'], 1)
		res =  self.client.get('/actividad/')
		self.assertContains(res,"actividadTest")
		self.assertEqual(res.status_code, 200)
