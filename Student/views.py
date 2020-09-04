from django.shortcuts import render,redirect

from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required  

@login_required(login_url='connect')
def index(request):
	text = "Bonjour le monde"
	text2 = "Moi c'est Herve"
	nummber = 25769393905

	return render(request, "index.html", locals())

def profile(request):
	text 
	
	return render(request, "profil.html", locals())

def registerSchool(request):
	school_form = SchoolForm(request.POST or None)
	if(request.method == 'POST'):
		if(school_form.is_valid()):
			school_form.save()
	school_form = SchoolForm()

	return render(request, "forms.html", locals())


def registerClass(request):
	classe_form = ClasseForm(request.POST or None)
	if(request.method == 'POST'):
		if(classe_form.is_valid()):
			classe_form.save()
	classe_form = ClasseForm()
	return render(request, "forms.html", locals())


def register(request):

	register_form = RegisterStudentForm(request.POST or None,request.FILES)

	if(request.method == 'POST'):

		if(register_form.is_valid()):
			register_form.save()
			
	register_form = RegisterStudentForm()
	return render(request, "forms.html", locals())

def register_profil(request):

	profil_form=ProfileForm(request.POST or None, request.FILES)
	if (request.method=='POST'):
		if (profil_form.is_valid()):
			username=profil_form.cleaned_data['username']
			password=profil_form.cleaned_data['password']
			password1=profil_form.cleaned_data['password1']
			nom=profil_form.cleaned_data['nom']
			prenom=profil_form.cleaned_data['prenom']
			age=profil_form.cleaned_data['age']
			matricule=profil_form.cleaned_data['matricule']
			photo=profil_form.cleaned_data['photo']

			if (password==password1):
				user=User.objects.create_user(username=username, password=password)
				user.first_name=nom
				user.last_name=prenom
				user.save()
				profil=Profil(user=user, age=age, matricule= matricule, photo=photo).save()
				if user:
					login(request, user)
					return redirect(index)
				else:
					return redirect(connexion)
			else:
				profil_form=ProfileForm(request.FILES)

	profil_form=ProfileForm(request.FILES)
	return render(request, 'forms.html',locals())

def connexion(request):
	connexion_form=ConnexionForm(request.POST)
	if (request.method == 'POST'):
		if connexion_form.is_valid():
			username=connexion_form.cleaned_data['username']
			password=connexion_form.cleaned_data['password']
			user=authenticate(username=username,password=password)#verification donnée
			if user:#si l'objet existe 
				login(request, user)
				return redirect(index) #on connecte l'utilisateur
			else:
				connexion_form=ConnexionForm()
	else:
		connexion_form=ConnexionForm()	
	return render(request, 'forms.html',locals())
def deconnexion(request):
	logout(request)
	return redirect(connexion)

def ListStudent(request):
	students = RegisterStudent.objects.all()

	return render(request, "lists.html", locals())


def modifier(request,student_id):
	student = RegisterStudent.objects.get(id=student_id)

	modifier_form = RegisterStudentForm(request.POST or None,request.FILES, instance=student)
	if(request.method == 'POST'):

		if(modifier_form.is_valid()):
			modifier_form.save()
			return redirect(ListStudent)
	modifier_form = RegisterStudentForm(instance=student)
	return render(request, "forms.html", locals())
	

def Delete(request,student_id):
	student = RegisterStudent.objects.get(id=student_id)
	student.delete()
	return redirect(ListStudent)