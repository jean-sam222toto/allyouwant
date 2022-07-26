import imp
from django.urls import path
from . views import *

urlpatterns= [
    path("articles", page_garde, name='page de garde'),
    #path("<str:nom>", nom_user, name="Formate l'url utilisateur")
]