from django.test import TestCase

from plantilla_de_flujo.models import plantilla_de_flujo
from scrummer.models import Usuario


# Create your tests here.
def crear_usuario(nombre, apellido, nombreUsuario, contrasenha, direccion, correo, telefono, observacion, estado,
                  roles):
    """
	Funcion: Encargada de crear un usuario para la realizacion de pruebas
	"""
    return Usuario.objects.create(nombre='Juan', apellido='Valdez', nombreUsuario='usuario1',
                                  contrasenha='usu1', direccion='Pedro Getto 548',
                                  correo=4100100, telefono=45848565, observacion='Desarrollador de Django',
                                  estado='activo', roles='desarrollador'
                                  )


def crear_plantilla_de_flujo(nombre, actividades):
    """
	Funcion: Encargada de crear una plantilla de flujo para realizacion de pruebas
	"""
    return plantilla_de_flujo.objects.create(nombre=nombre)


class PlantilladeFlujoTest(TestCase):
    def test_creacion_plantilla_de_flujo(self):
        """
		Se comprueba que la plantilla de flujo es creada exitosamente
		"""
        plantillatest = crear_plantilla_de_flujo("plantilla de flujo de prueba", "actividad1,actividad2,actividad3")
        tplantilla = plantilla_de_flujo.objects.get(nombre="plantilla de flujo Test")
        self.assertEqual(tplantilla.nombre, "plantilla de flujo Test")

    def test_eliminacion_plantilla_de_flujo(self):
        """
		Se comprueba la eliminacion de la plantilla de flujo
		"""
        plantillatest = crear_plantilla_de_flujo("plantilla de flujo de prueba")
        plantillatest.save()
        self.assertEqual(len(plantillatest), 0)

    def test_conexion(self):
        usuario = crear_usuario('admin', 'admin')
        usuario.save()
        f = crear_plantilla_de_flujo("Plantilla de flujo", "actividad1,actividad2,actividad3")
        f.save()
        res = self.client.post('/login/', {'username': 'admin', 'password': 'admin'})
        tsession = self.client.session
        print 'data'
        print tsession
        print tsession['usuario']
        print res
        self.assertEqual(tsession['usuario'], 1)
        res = self.client.get('/plantilla_de_flujo/')
        self.assertContains(res, "plantillaTest")
        self.assertEqual(res.status_code, 200)
