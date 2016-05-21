

from django.test import TestCase
from flujo.models import flujo
from proyecto.models import proyecto





class FlujoTest(TestCase):


    def setUp(self):
        print "\nTEST FLUJO"


        flujoprueba = flujo.objects.create(nombre='flujo de app para moviles', proyecto= proyecto.objects.create(nombre=nombre, descripcion=descripcion,
								 fecha_inicio=2016-01-01,
								 fecha_fin=2016-10-10,
								 ))
        flujoprueba.save()

        print("Se creo el flujo ")



    def test_ABMFlujo(self):

        print "\n----------Se procede a buscar la fase de prueba creada"
        valido = flujo.objects.filter(nombre="desarrollo de app para moviles").exists()
        if valido:
            print "\nSe encontro el flujo creado"
        if valido==False:
            print "\nNo se ha creado el flujo"
        print "\n----------Ahora se busca un flujo que no existe"

        valido=proyecto.objects.filter(nombre="flujopruebanoexiste").exists()
        if valido==False:
            print "\nNo existe el flujo "
        print "\n----------Se procede a buscar el flujo creado para modificar su nombre"
        valido = flujo.objects.filter(nombre="faseprueba").exists()
        if valido:
            print "\nSe encontro el flujo y se procedera a cambiar el valor del campo nombre"
            flujo.objects.filter(nombre="flujoprueba").update(nombre ="flujo de software para E-Commerce")
            valido = flujo.objects.filter(nombre="flujo de software para  E-Commerce").exists()
            if valido:

                print "\nEl flujo fue modificado adecuadamente con nombre \'flujo de software para E-Commerce\'"

        print "\n----------Se procede a borrar el flujo "
        valido = False
        valido= flujo.objects.filter(nombre="flujo de software para E-Commerce").exists()
        if valido:
                flu = flujo.objects.filter(nombre="flujo de software para E-Commerce")
                flu.delete()
                print "\nFlujo Borrado"
        if valido==False:
             print "Error al borrar el flujo, se debe dar un nombre de flujo existente"