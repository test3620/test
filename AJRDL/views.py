from django.shortcuts import render

""" PAGE D'ACCUEIL """
def accueil_view(request):
    return render(request, 'index.html')

""" PAGE DE A PROPOS """
def a_propos_view(request):
    return render(request, 'a_propos.html')

""" PAGE DU BUREAU """
def bureau_view(request):
    return render(request, 'bureau.html')

""" PAGE DE COTISATION """
def cotisation_view(request):
    return render(request, 'cotisation.html')

""" PAGE D'ACTUALITÉ """
def actualite_view(request):
    return render(request, 'actualite.html')

""" PAGE D'INSCRIPTION' """
def inscription_view(request):
    return render(request, 'inscription.html')

""" PAGE DE CONTACT """
def contact_view(request):
    return render(request, 'contact.html')