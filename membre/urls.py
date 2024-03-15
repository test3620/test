""" IMPORTATION DES MODULES """
from django.urls import path 
from .views import membre_view # PAGES : MEMBRE,

"""
from django.conf import settings
from django.conf.urls.static import static
"""

urlpatterns = [
    path('espace membre', membre_view, name='membre'), # Lchemin de la page membre.html
]



"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

"""
