from django import forms
from .models import *

class SchoolForm(forms.ModelForm):

	class Meta:
		model = School
		fields = '__all__'


class ClasseForm(forms.ModelForm):

	class Meta:
		model = Classe
		fields = '__all__'
		


class RegisterStudentForm(forms.ModelForm):
	
	class Meta:
		model = RegisterStudent
		fields = '__all__'

class ProfileForm(forms.Form):
	#____________pour user___________________#
		username=forms.CharField(max_length=20)
		password=forms.CharField(max_length=20, widget=forms.PasswordInput)
		password1=forms.CharField(max_length=20, widget=forms.PasswordInput)
		nom=forms.CharField(max_length=20)
		prenom=forms.CharField(max_length=20)
#_________________champ pou profil_______________#
		age =forms.IntegerField()
		matricule=forms.CharField(max_length=20)
		photo = forms.ImageField()

class ConnexionForm(forms.Form):
	username= forms.CharField(label="Nom d'utilisateur :", max_length=20)
	password = forms.CharField(label="mot de passe :", widget= forms.PasswordInput)
	
		