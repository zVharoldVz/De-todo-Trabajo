from email.mime import image
from multiprocessing.sharedctypes import Value
from xml.dom.minidom import Attr
from django import forms
from django.forms import HiddenInput, fields
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic.edit import UpdateView
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import *

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True,'autofocus' : True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True}))
    remember_me = forms.BooleanField(required=False)

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True,'autofocus' : True}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','required': True}))
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True}))
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required': True}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }

class UserEditForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name']
		
class ExtraEditForm(forms.ModelForm):
	telefono = forms.IntegerField(required=True,validators=[MinValueValidator(1000000),MaxValueValidator(9999999999)], widget= forms.NumberInput(attrs={'class':'form-control'}))
	dni = forms.IntegerField(required=True,validators=[MaxValueValidator(99999999)], widget= forms.NumberInput(attrs={'class':'form-control'}))
	Direcion = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = ExtraDato
		fields = ['telefono', 'dni', 'Direcion']

class UploadImageusaerForm(forms.ModelForm):

    class Meta:
        model = Foto_perfil
        fields = ['imagen']

class habilidadesfrom (forms.ModelForm):

	nombrehabilidad = forms.CharField(required=True,max_length=50, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su habilidad',"aria-describedby":"id_nombrehabilidad"}))
	descripcion = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Ingrese su descripcion','style':'height: 100px'}))
	tipoTrabajo = forms.ModelChoiceField(queryset=TipoTrabajo.objects.all(), initial='Seleccione un tipo de trabajo', widget=forms.Select(attrs={'class': 'form-select'}))
	class Meta:
		model = Habilidades
		fields =['nombrehabilidad','descripcion','tipoTrabajo']

class habilidadesFullForm(habilidadesfrom):
	images = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control','multiple': True,'id':'seleccionArchivos'}))

	class Meta(habilidadesfrom.Meta):
		fields = habilidadesfrom.Meta.fields + ['images',]

