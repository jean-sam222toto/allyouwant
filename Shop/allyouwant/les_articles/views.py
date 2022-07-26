import imp
from django.http import HttpResponse
from django.shortcuts import render
from les_articles.models import Articles

# Create your views here.

def page_garde(request):
    return render(request, 'les_articles/articles.html')

def nom_user(request, nom):
    return HttpResponse(f"Salut {nom}")