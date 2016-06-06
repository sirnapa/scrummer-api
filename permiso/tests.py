
from django.test import TestCase


from permiso.models import permiso
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
def crear_permiso(nombre):
	"""
	Funcion: Encargada de crear un permiso para realizacion de pruebas
	"""
	return permiso.objects.create(nombre=nombre)

class PermisoTest(TestCase):

	def test_creacion_permiso(self):
		"""
		Se comprueba que el permiso es creado exitosamente
		"""
		permisotest = crear_permiso("permiso de prueba")
		tpermiso = permiso.objects.get(nombre="permisoTest")
		self.assertEqual(tpermiso.nombre, "permisoTest")

	def test_eliminacion_permiso(self):
		"""
		Se comprueba la eliminacion del permiso
		"""
		permisotest = crear_permiso("permisoTest")
		permisotest.save()
		self.assertEqual(len(permisotest), 0)

	def test_conexion(self):


		usuario = crear_usuario('admin', 'admin')
		usuario.save()
		f = crear_permiso("Lectura")
		f.save()
		res = self.client.post('/login/',{'username':'admin','password':'admin'})
		tsession = self.client.session
		print 'data'
		print tsession
		print tsession['usuario']
		print res
		self.assertEqual(tsession['usuario'], 1)
		res =  self.client.get('/permiso/')
		self.assertContains(res,"permisoTest")
		self.assertEqual(res.status_code, 200)