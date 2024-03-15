from django.shortcuts import render
from .models import Membres

""" PAGE DE MEMBRE """
def membre_view(request):
    membre = Membres.objects.all()
    return render(request, 'membre/membre.html', {'membre': membre})
