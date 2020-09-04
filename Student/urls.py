from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home"),
    path('profile/', views.profile, name="profil"),
    path('enregisterement/', views.register, name='register'),
    path('addSchool/', views.registerSchool, name='addSchool'),
    path('addClass/', views.registerClass, name="addClass"),
    path('listEtudiant/', views.ListStudent, name='listeE'),
    path('modifierET/<int:student_id>/', views.modifier, name='modifE'),
    path('DeleteET/<int:student_id>/', views.Delete, name='deleteET'),
    path('register_profil/', views.register_profil, name='profil'),
    path('connexion/', views.connexion, name='connect'),
    path('deconnexion/', views.deconnexion, name='deconnect'),



]
