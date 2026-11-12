from django.shortcuts import render

def index(request):
    return render(request, 'WymowkiStudenckie/index.html')

def DodajWymowke(request):
    return render(request, "WymowkiStudenckie/dodaj_wymowke.html")

def Ranking(request):
    return render(request, "WymowkiStudenckie/ranking.html")

def logowanie(request):
    return render(request, "WymowkiStudenckie/logowanie.html")

def rejestracja(request):
    return render(request, "WymowkiStudenckie/rejestracja.html")

def profil(request):
    return render(request, "WymowkiStudenckie/profil.html")