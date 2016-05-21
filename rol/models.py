from __future__ import unicode_literals
from django.db import models as modelsdb
from permiso.models import permiso
from proyecto.models import proyecto
from django.contrib.auth import models
from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType





class rol(modelsdb.Model):

    """Clase rol"""

    class Meta:
     verbose_name = 'rol'
     verbose_name_plural = 'roles'






    #permission5 = Permission.objects.create(codename='LISTAR_PROYECTOS',
    #                                         name='Listar proyectos', content_type_id =10,
    #                                        )

    #permission6 = Permission.objects.create(codename='AGREGAR_PROYECTOS',
                    #                         name='Agregar proyectos', content_type_id =10,
                     #                       )
    #permission7 = Permission.objects.create(codename='EDITAR_PROYECTOS',
                      #                       name='Editar Proyectos',content_type_id =10,
                       #                     )
    #permission8 = Permission.objects.create(codename='ELIMINAR_PROYECTOS',
                        #                     name='Eliminar proyectos',content_type_id =10,
                         #                   )

    #permission9 = Permission.objects.create(codename='LISTAR_FLUJO',
     #                                        name='Listar flujos',content_type_id =14,
     #                                       )


    #permission10 = Permission.objects.create(codename='AGREGAR_FLUJO',
                          #              name='Agregar flujos',content_type_id =14,
                           #             )
    #permission11 = Permission.objects.create(codename='EDITAR_FLUJO',
                            #            name='Editar flujos',content_type_id =14,
                             #           )
    #permission12 = Permission.objects.create(codename='ELIMINAR_FLUJO',
                              #          name='Eliminar flujos',content_type_id =14,
                               #         )

    #permission13 = Permission.objects.create(codename='LISTAR_USERSTORY',
    #                                         name='Listar User Stories',content_type_id =12,
    #                                         )


    #permission14 = Permission.objects.create(codename='AGREGAR_USERSTORY',
     #                                   name='Agregar User Story',content_type_id =12,
      #                                  )
    #permission15 = Permission.objects.create(codename='EDITAR_USERSTORY',

        #                               name='Editar user story', content_type_id =12,
       #                                 )
    #permission16 = Permission.objects.create(codename='ELIMINAR_USERSTORY',
     #                                   name='Eliminar user story', content_type_id =12,
      #                                  )

    #permission17 = Permission.objects.create(codename='LISTAR_SPRINT',content_type_id =13,
    #                                         name='Listar sprint',
    #                                         )


    #permission18 = Permission.objects.create(codename='AGREGAR_SPRINT',
     #                                   name='Agregar sprint',content_type_id =13,
      #                                  )
    #permission19 = Permission.objects.create(codename='EDITAR_SPRINT',
    #                                    name='Editar sprint',content_type_id =13,
     #
      #                                  )
    #permission20 = Permission.objects.create(codename='ELIMINAR_SPRINT',
     #                                   name='Eliminar sprint', content_type_id =13,
      #                                  )

    ROL = (
         ('0', 'DESARROLLADOR'),
         ('1', 'SCRUM_MASTER'),
         ('2', 'ADMINISTRADOR'),
     )
    nombre = modelsdb.CharField(max_length=1, choices=ROL, default=0)
    #nombre = models.SmallIntegerField(choices=NOMBRE_CHOICES)
    #permisos = models.ManyToManyField('permiso.permiso', blank=True, default=None)
    proyecto = modelsdb.ForeignKey(proyecto, null=True, blank=True, default=None)
    permisos_del_rol = modelsdb.ManyToManyField(
         models.Permission,
         verbose_name=('permisos_del_rol'),
         blank=True,
         help_text=('Especifica permisos del rol'),
         related_name="rol_set",
         related_query_name="user",
    )
    def __unicode__(self):
     return self.nombre