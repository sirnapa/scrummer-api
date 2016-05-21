

from django.test import TestCase
from django.utils import timezone
from proyecto.models import proyecto
from rol.models import rol
from permiso.models import permiso
from scrummer.models import Usuario

# Create your tests here.

def crear_proyecto(nombre, descripcion, fecha_creacion, complejidad_total, estado):
	"""
    Funcion: Encargada de crear un proyecto para realizacion de pruebas
	"""
	return proyecto.objects.create(nombre=nombre, descripcion=descripcion,
								 fecha_inicio=2016-01-01,
								 fecha_fin=2016-10-10,
								 )

def crear_rol(nombre, descripcion):
	"""
	Funcion: Encargada de crear un rol para realizacion de pruebas
	"""
	return rol.objects.create(nombre=nombre, descripcion=descripcion)

def crear_permiso(nombre):
	"""
	Funcion: Encargada de crear un permiso para la realizacion de pruebas
	"""
	return permiso.objects.create(nombre=nombre)

def crear_usuario(username, password):
	"""
	Funcion: Encargada de crear un usuario para la realizacion de pruebas
	"""
	return Usuario.objects.create(nombre='Juan',
								apellido='Gonzalez', nombreUsuario='usuario1' , contrasenha= '123',direccion='Mcal Lopez 154',
                                telefono='458756535',observacion='Incorporado al proyecto desde el primer dia',
								estado=True, email='ts1@mail.com',roles = ['desarrollador',]
								)

class proyectoTest(TestCase):

	def test_creacion_proyecto(self):
		"""
		Se comprueba que el proyecto es creado exitosamente
		"""
		p = crear_proyecto("proyectoTest","Prueba de test.py", timezone.now(), 0, "no iniciado")
		tp = proyecto.objects.get(nombre="proyectoTest")
		self.assertEqual(tp.nombre, "proyectoTest")


    def test_editar_proyecto(self):
        c = self.client
        self.assertTrue(c.login(username='juan', password='developer'))
        response = c.get('/proyectos/modificar/1')
        self.assertEquals(response.status_code, 200)
        p = proyecto.objects.get(pk=1)
        p.nombre = 'Scrummer'
        p.save(update_fields=['nombre'])
        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(proyecto.objects.get(nombre='Scrummer'))

    def test_eliminacion_proyecto(self):
		"""
		Se comprueba que al eliminar el proyecto, todos los roles
		asociado al mismo tambien son eliminados
		"""
		p = crear_proyecto("proyectoTest","Prueba de test.py", timezone.now(), 0)
		p.save()
		r = crear_rol("Administrador proyectoTest", "rol de prueba")
		r.proyecto = p
		r.save()
		pr = crear_permiso("crear",0)
		r.permisos.add(pr)
		pr = crear_permiso("modificar",0)
		r.permisos.add(pr)

		proyecto.objects.get(nombre="proyectoTest").delete()
		tp = proyecto.objects.all()
		r = rol.objects.all()
		self.assertEqual(len(tp), 0)
		self.assertEqual(len(r), 0)


