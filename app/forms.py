import email
from email.mime import image
from multiprocessing.sharedctypes import Value
from pyexpat import model
import re
from statistics import mode
from sys import maxsize
from xml.dom.minidom import Attr
from django import forms
from django.forms import HiddenInput, fields
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic.edit import UpdateView
from django.core.validators import MinValueValidator, MaxValueValidator
from bootstrap_modal_forms.forms import BSModalModelForm 
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.contrib.auth import get_user_model
from .models import *

User =get_user_model()
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True,'autofocus' : True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True}))
    remember_me = forms.BooleanField(required=False)

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True,'autofocus' : True}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True}))
	password1 = forms.CharField(label='Contraseña',help_text='Debe contener MAYUSCULAS, minusculas y numero, minimo 9 caracteres', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True}))
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		
	def clean(self):
		# data from the form is fetched using super function
		super(UserRegisterForm, self).clean()
		# extract the username and text field from the data
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')
		# conditions to be met for the username length
		#if len(username) < 5:
		#	self._errors['username'] = self.error_class(['Mínimo 5 caracteres requeridos'])
			
		#if User.objects.filter(username=username).exists():
		#	self._errors['email'] = self.error_class(['El usuario ya se encuentra registrado'])	

		if User.objects.filter(email=email).exists():
			self._errors['email'] = self.error_class(['Ya existe este correo registrado porfavor ingrese otro.'])

		# return any errors if found
		return self.cleaned_data

class UserEditForm(BSModalModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	telefono = forms.IntegerField(required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
	dni = forms.IntegerField(required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
	Direcion = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

	distrito = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
	provincia = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
	departamento = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
	pais = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ['first_name','last_name','telefono', 'dni', 'Direcion','distrito','provincia', 'departamento', 'pais']
	def clean(self):
		# data from the form is fetched using super function
		super(UserEditForm, self).clean()
		# extract the username and text field from the data
		dni = self.cleaned_data.get('dni')
		telefono = self.cleaned_data.get('telefono')

		DNI_string = str(dni)
		DNilength = len(DNI_string)
		Tele_string = str(telefono)
		telelength = len(Tele_string)
		print(DNI_string)
		# conditions to be met for the username length
		if DNilength >= 9:
			self._errors['dni'] = self.error_class(['El DNI no puede ser mayor de 8 dijitos'])
		elif DNilength <=7 :
			self._errors['dni'] = self.error_class(['El DNI no puede ser menor de 8 dijitos'])
		elif DNilength == 0 :
			self._errors['dni'] = self.error_class(['El DNI no puede estar vacio'])

		if telelength > 10:
			self._errors['telefono'] = self.error_class(['El DNI no puede ser mayor de 10 dijitos'])

		# return any errors if found
		return self.cleaned_data


class UploadImageusaerForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['imagen']

class habilidadesfrom (BSModalModelForm):

	nombrehabilidad = forms.CharField(required=True,max_length=50, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su habilidad',"aria-describedby":"id_nombrehabilidad"}))
	descripcion = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Ingrese su descripcion','style':'height: 150px'}))
	tipoTrabajo = forms.ModelChoiceField(queryset=TipoTrabajo.objects.all(), initial='Seleccione un tipo de trabajo', widget=forms.Select(attrs={'class': 'form-select'}))
	class Meta:
		model = Habilidades
		fields =['nombrehabilidad','tipoTrabajo','descripcion']

class habilidadesFullForm(habilidadesfrom,BSModalModelForm):
	images = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control','multiple': True,'id':'seleccionArchivos'}))

	class Meta(habilidadesfrom.Meta):
		fields = habilidadesfrom.Meta.fields + ['images',]


class Valoracionfrom (forms.ModelForm):

	comentario = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Ingrese su descripcion','style':'height: 100px'}))
	puntuacion = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'class': 'result'}))

	class Meta:
		model = Clasifiacion
		fields =['comentario','puntuacion']

class ValoracionFullForm(Valoracionfrom):

	fotoValoracion = forms.FileField(required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control','multiple': True,'id':'seleccionArchivos'}))

	class Meta(Valoracionfrom.Meta):
		fields = Valoracionfrom.Meta.fields + ['fotoValoracion']

