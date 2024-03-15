from django.shortcuts import render

""" PAGE D'ACCUEIL """
def accueil_view(request):
    return render(request, 'index.html')

""" PAGE DE A PROPOS """
def a_propos_view(request):
    return render(request, 'a_propos.html')