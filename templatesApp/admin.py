from django.contrib import admin
from templatesApp.models import Profesor
from templatesApp.models import Apoderado
from templatesApp.models import Alumnos


class ProfesorAdmin(admin.ModelAdmin):
    list_display=['id','nombre','edad','curso_asignado','fechaInicio','fechatermino','saldo']
# Register your models here.


admin.site.register(Profesor,ProfesorAdmin)

class ApoderadoAdmin(admin.ModelAdmin):
    list_display=['id','nombre','rut','edad','telefono','SegundoApoderado','telefono2']
# Register your models here.
admin.site.register(Apoderado,ApoderadoAdmin)

class AlumnosAdmin(admin.ModelAdmin):
    list_display=['id','nombre','rut','edad','curso','telefono','correo','profesor','apoderado']
admin.site.register(Alumnos,AlumnosAdmin)