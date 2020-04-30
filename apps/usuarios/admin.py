from django.contrib import admin
from .models import Usuario,Computadora
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class UserRecursos(resources.ModelResource):
	class Meta:
		model = Usuario

class CompuRecursos(resources.ModelResource):
	class Meta:
		model = Computadora

class UsuariosMejor(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ["nombre", "apellido_paterno", "telefono"]
	list_display = ("nombre", "apellido_paterno", "telefono", "fecha_creacion",)
	resource_class = UserRecursos

class CompusMejor(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ["nombre", "serie", "costo"]
	list_display = ("nombre", "serie", "costo", "fecha_creacion",)
	resource_class = CompuRecursos

admin.site.register(Usuario, UsuariosMejor)
admin.site.register(Computadora, CompusMejor)

