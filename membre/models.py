from django.db import models

""" LE MODEL DE MEMBRE """
class Membres(models.Model):
    nom = models.CharField(("NOM :"), max_length=50)
    prenom = models.CharField(("PÉNOM :"), max_length=50)
    profession =models.CharField(("PROFESSION :"), max_length=50)
    ville_natale = models.CharField(("vILLE NATALE :"), max_length=50)
    age = models.IntegerField(("AGE :"))
    date_adhesion = models.DateTimeField(("DATE D'ADESION :"), auto_now=False, auto_now_add=True)
    image = models.ImageField(("IMAGE :"), upload_to='images', height_field=None, width_field=None, max_length=None, blank=False)





