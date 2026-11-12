from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('DodajWymowke/', views.DodajWymowke, name="DodajWymowke"),
    path('Ranking/', views.Ranking, name="Ranking"),
    path('logowanie/', views.logowanie, name="logowanie"),
    path('rejestracja/', views.rejestracja, name="rejestracja"),
    path('profil/', views.profil, name="profil"),
]