from distutils.command.upload import upload
from operator import truediv
from pyexpat import model
from django.db import models

"""
Caratéristiques des articles
- Nom string
- Prix float 
- Disponibilité boolean
- Quantité en stock int 
- Description text
- Image 

"""
class Articles(models.Model):
    nom_article = models.CharField(max_length=100)
    prix_article = models.FloatField(default=0.0)
    disponible_article = models.BooleanField(default=True)
    quantite_en_stock = models.IntegerField(default=0)
    memo_article = models.TextField(max_length=500, blank=True)
    image_article = models.ImageField(upload_to= "dir_image_article", blank= True, null=True)

    def __str__(self):
        return f'{self.nom_article} ({self.quantite_en_stock})'