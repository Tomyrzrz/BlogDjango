from django import forms
from .models import Usuario,Computadora

class UserForm(forms.ModelForm):
	
	class Meta:
		model = Usuario
		fields = ['nombre','apellido_paterno','apellido_materno','direccion','telefono']

class CompuForm(forms.ModelForm):
		
	class Meta:
		model = Computadora
		fields = ['nombre','serie','detalles','costo']
				
		





