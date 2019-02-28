from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.forms.models import modelformset_factory
from decimal import *
from listes_de_prix.models import Fournisseur, Machine, Option
from listes_de_prix.forms import *
from ressources.models import Devise


def liste_fournisseurs(request):
    liste_fournisseurs = Fournisseur.objects.all().order_by('-actif', 'nom')
    return render(request, 'listesdeprix/liste_fournisseurs.html', {'liste_fournisseurs': liste_fournisseurs})


def detail_fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    return render(request, 'listesdeprix/detail_fournisseur.html', {'fournisseur': fournisseur})        


@permission_required('listes_de_prix.afficher_listes_prix')
def liste_machines(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    liste_machines = Machine.objects.filter(fournisseur=fournisseur, actif=True).order_by('categorie', 'numero')
    return render(request, 'listesdeprix/liste_machines.html', {'liste_machines': liste_machines,
                                                                'fournisseur': fournisseur})


@permission_required('listes_de_prix.afficher_listes_prix')
def details_machine(request, fournisseur_id, machine_id):
    machine = Machine.objects.get(id=machine_id)
    liste = list()
    liste.append(machine)
    total = {'liste': liste, 'prix_fournisseur': machine.prix_fournisseur, 'plMin': Decimal(machine.plMin()),
             'cost': Decimal(machine.cost()), 'profit': Decimal(machine.profit()),
             'profit_pourcent': Decimal(machine.profit_pourcent())}
    OptionFormSet = modelformset_factory(Option, extra=0, form=OptionForm)
    if request.method == 'POST':
        formset = OptionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data['calcul']:
                    option = Option.objects.get(numero=form.cleaned_data['numero'])
                    total['liste'].append(option)
                    total['plMin'] += Decimal(option.plMin())
                    total['prix_fournisseur'] += Decimal(option.prix_fournisseur)
                    total['cost'] += Decimal(option.cost())
                    total['profit'] += Decimal(option.profit())
                    total['profit_pourcent'] = format(total['profit'] / total['plMin'] * 100, '.2f')
            return render(request, 'listesdeprix/details_machine.html', {'machine': machine, 'formset': formset,
                                                                         'total': total})
    else:
        formset = OptionFormSet(queryset=machine.options_machine.all())
    return render(request, 'listesdeprix/details_machine.html', {'machine': machine, 'formset': formset,
                                                                 'total': total})


@permission_required('listes_de_prix.afficher_listes_prix_en')
def liste_machines_en(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    liste_machines = Machine.objects.filter(fournisseur=fournisseur, actif=True).order_by('categorie', 'numero')
    taux_us = Devise.objects.get(code_iso="USD")
    return render(request, 'listesdeprix/liste_machines_en.html', {'liste_machines': liste_machines,
                                                                   'fournisseur': fournisseur, 'taux_us':taux_us})


@permission_required('listes_de_prix.afficher_listes_prix_en')
def print_liste_machines_en(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    liste_machines = Machine.objects.filter(fournisseur=fournisseur, actif=True).order_by('categorie', 'numero')
    return render(request, 'listesdeprix/print_liste_machines_en.html', {'liste_machines': liste_machines,
                                                                         'fournisseur': fournisseur})

@permission_required('listes_de_prix.afficher_listes_prix')
def print_liste_machines(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    liste_machines = Machine.objects.filter(fournisseur=fournisseur, actif=True).order_by('categorie', 'numero')
    return render(request, 'listesdeprix/print_liste_machines.html', {'liste_machines': liste_machines,
                                                                         'fournisseur': fournisseur})

@permission_required('listes_de_prix.afficher_listes_prix_en')
def details_machine_en(request, fournisseur_id, machine_id):
    machine = Machine.objects.get(id=machine_id)
    liste = list()
    liste.append(machine)
    total = {'liste': liste, 'prix_fournisseur': machine.prix_fournisseur, 'plMin': Decimal(machine.plMinUS()),
             'cost': Decimal(machine.cost()), 'profit': Decimal(machine.profitUs()),
             'profit_pourcent': Decimal(machine.profit_pourcentUs())}
    OptionFormSet = modelformset_factory(Option, extra=0, form=OptionForm)
    if request.method == 'POST':
        formset = OptionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data['calcul']:
                    option = Option.objects.get(numero=form.cleaned_data['numero'])
                    total['liste'].append(option)
                    total['plMin'] += Decimal(option.plMinUS())
                    total['prix_fournisseur'] += Decimal(option.prix_fournisseur)
                    total['cost'] += Decimal(option.cost())
                    total['profit'] += Decimal(option.profitUs())
                    total['profit_pourcent'] = total['profit'] / total['plMin'] * 100
            return render(request, 'listesdeprix/details_machine_en.html', {'machine': machine, 'formset': formset,
                                                                            'total': total})
    else:
        formset = OptionFormSet(queryset=machine.options_machine.all())
    return render(request, 'listesdeprix/details_machine_en.html', {'machine': machine, 'formset': formset,
                                                                 'total': total})