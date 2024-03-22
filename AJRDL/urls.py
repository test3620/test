""" IMPORTATION DES MODULES """
from django.contrib import admin
from django.urls import path, include 
from .views import accueil_view, a_propos_view, bureau_view, cotisation_view, actualite_view, inscription_view, contact_view # PAGES : ACCUEIL, A PROPOS, BUREAU, COTISATION, ACTUALITE, INSCRIPTION, CONTACT


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil_view, name='accueil'), # Le chemin vers la page d'accueil
    path('a propos/', a_propos_view, name='a_propos'), # Le chemin vers la page de à propos
    path('bureau/', bureau_view, name='bureau'), # Le chemin vers la page du bureau
    path('cotisation/', cotisation_view, name='cotisation'), # Le chemin vers la page de cotisqtion
    path('actualite/', actualite_view, name='actualite'), # Le chemin vers la page d'actualité
    path('inscription/', inscription_view, name='inscription'), # Le chemin vers la page d'inscription
    path('contact/', contact_view, name='contact'), # Le chemin vers la page de contact
    path('membre/', include('membre.urls')), # Le chemin vers la page des membres
]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
