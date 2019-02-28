from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from budget_materiel.models import Materiel_Eugenie, Fournisseur
from django.db.models import Sum


@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')
def view_fournisseurs_materiels(request):
    fournisseurs = Fournisseur.objects.all().annotate(total=Sum('materiel_eugenie__montant')).order_by('nom')
    return render(request,"materiels/view_fournisseurs_materiels.html",{"fournisseurs":fournisseurs})

@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')
def fournisseurs_materiels_details(request, fournisseur_id):
    projets = Materiel_Eugenie.objects.filter(fournisseur__id=fournisseur_id).values('projet__numero','fournisseur__nom','categorie__nom','montant').annotate(total=Sum('montant')).order_by('projet__numero')
    return render(request,"materiels/fournisseurs_materiels_details.html",{"projets":projets})
