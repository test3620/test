""" IMPORTATION DES MODULES """
from django.contrib import admin
from django.urls import path, include 
from .views import accueil_view, a_propos_view # PAGES : ACCUEIL, A PROPOS 


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil_view, name='accueil'), # Le chemin vers la page d'accueil
    path('a propos/', a_propos_view, name='a_propos'), # Le chemin vers la page de à propos
    path('membre/', include('membre.urls')), # Le chemin vers la page des membres
]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
