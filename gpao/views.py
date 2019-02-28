from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from gpao.models import Nm, Pe, Piece, Famille
from gpao.forms import *
from operator import itemgetter


def main_gpao(request):
    return render(request, "gpao/main_gpao.html")


def liste_nm(request):
    liste_nm = Nm.objects.all().order_by('reference')
    return render(request, "gpao/liste_nm.html", {'liste_nm': liste_nm})


def details_nm(request, no_nm):
    nm = Nm.objects.get(reference=no_nm)
    return render(request, "gpao/details_nm.html", {'nm': nm})


def liste_pe(request):
    liste_pe = Pe.objects.all().order_by('reference')
    return render(request, "gpao/liste_pe.html", {'liste_pe': liste_pe})


def liste_piece(request):
    liste_piece = Piece.objects.all().order_by('famille', 'reference')
    return render(request, "gpao/liste_piece.html", {'liste_piece': liste_piece})


def liste_famille(request):
    liste_famille = Famille.objects.all().order_by('reference')
    return render(request, "gpao/liste_famille.html", {'liste_famille': liste_famille})


def famille_piece(request, famille):
    pieces = Piece.objects.filter(famille__reference = famille)
    return render(request, "gpao/famille_piece.html", {'pieces': pieces})


def details_piece(request, no_piece):
    piece = Piece.objects.get(reference=no_piece)
    return render(request, "gpao/details_piece.html", {'piece': piece})


def soumission(request, no_nm):
    nm = Nm.objects.get(reference=no_nm)
    formset_init = []
    liste_qt = nm.get_pieces_list()
    #liste_qt = sorted(liste_qt, key=itemgetter('ref'))
    for piece in liste_qt:
        formset_init.append({'choix': False, 'piece': piece['piece'].id, 'qt': piece['qt']})

    if request.method == 'POST':  # If the form has been submitted...
        formset = SoumissionFormset(request.POST)
        if formset.is_valid():  # All validation rules pass
            return render(request, 'gpao/demandesoumission.html', {'formset': formset, 'no_nm': no_nm, })
    else:
        formset = SoumissionFormset(initial=formset_init)

    return render(request, 'gpao/soumission.html', {'formset':formset, 'no_nm': no_nm, })