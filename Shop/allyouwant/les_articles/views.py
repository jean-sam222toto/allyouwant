from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def page_garde(request):
    return render(request, 'les_articles/articles.html')