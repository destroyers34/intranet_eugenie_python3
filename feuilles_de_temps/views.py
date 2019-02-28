from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.forms.models import modelformset_factory
from feuilles_de_temps.models import Bloc_Eugenie, Bloc_TPE
from ressources.models import Employe
from feuilles_de_temps.forms import *
from django.db.models import Sum

@permission_required('feuilles_de_temps.add_bloc_eugenie')    
def blocs_eci(request):
    queryset = Bloc_Eugenie.objects.all()
    limit = 20
    count = queryset.count()
    if count > limit:
        last_blocs = queryset[count-limit:]
    else:
        last_blocs = queryset
    if request.method == 'POST':
        form = ConsultationBlocEugenieForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['employe']
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(emp.user.username) + '/' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str)
    else: 
        form = ConsultationBlocEugenieForm()
    return render(request,"feuillesdetemps/blocs_eci.html", {"last_blocs": last_blocs,'form':form})


@permission_required('feuilles_de_temps.add_bloc_tpe')
def blocs_tpe(request):
    queryset = Bloc_TPE.objects.all()
    limit = 20
    count = queryset.count()
    if count > limit:
        last_blocs = queryset[count-limit:]
    else:
        last_blocs = queryset
    if request.method == 'POST':
        form = ConsultationBlocTPEForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['employe']
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(emp.user.username) + '/' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str)
    else:
        form = ConsultationBlocTPEForm()
    return render(request,"feuillesdetemps/blocs_tpe.html", {"last_blocs": last_blocs,'form':form})


@permission_required('feuilles_de_temps.add_bloc_eugenie')   
def consultation_blocs_eci(request, username, date_debut, date_fin):
    blocs = Bloc_Eugenie.objects.filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).order_by('-date')
    if request.method == 'POST':
        form = ConsultationBlocEugenieForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['employe']
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = '../../../' + str(emp.user.username) + '/' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str)
    else: 
        form = ConsultationBlocEugenieForm()
    return render(request, 'feuillesdetemps/consultation_blocs_eci.html', {'blocs':blocs,'form':form,'username':username,'date_debut':date_debut,'date_fin':date_fin})   

@permission_required('feuilles_de_temps.add_bloc_tpe')
def consultation_blocs_tpe(request, username, date_debut, date_fin):
    blocs = Bloc_TPE.objects.filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).order_by('-date')
    if request.method == 'POST':
        form = ConsultationBlocTPEForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['employe']
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = '../../../' + str(emp.user.username) + '/' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str)
    else:
        form = ConsultationBlocTPEForm()
    return render(request, 'feuillesdetemps/consultation_blocs_tpe.html', {'blocs':blocs,'form':form,'username':username,'date_debut':date_debut,'date_fin':date_fin})

@permission_required('feuilles_de_temps.add_bloc_eugenie')    
def add_blocs_eci(request):
    BlocFormSet = modelformset_factory(Bloc_Eugenie, form=BlocEugenieForm)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("../success/")
    else:
        formset = BlocFormSet(queryset=Bloc_Eugenie.objects.none())
    return render(request,"feuillesdetemps/add_blocs_eci.html", {"formset": formset,})

@permission_required('feuilles_de_temps.add_bloc_tpe')    
def add_blocs_tpe(request):
    BlocFormSet = modelformset_factory(Bloc_TPE, form=BlocTPEForm)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("../success/")
    else:
        formset = BlocFormSet(queryset=Bloc_TPE.objects.none())
    return render(request, "feuillesdetemps/add_blocs_tpe.html", {"formset": formset,})
    
@login_required    
def success(request):
    return render(request, "feuillesdetemps/success.html")

@login_required
def add_success(request):
    return render(request, "feuillesdetemps/add_success.html")

@login_required
def edit_success(request):
    return render(request, "feuillesdetemps/edit_success.html")

#@permission_required('feuilles_de_temps.add_bloc_banque')
#def add_banque(request):
#    BanqueFormSet = modelformset_factory(Banque, form=BanqueForm)
#    if request.method == 'POST':
#        formset = BanqueFormSet(request.POST, request.FILES)
#        if formset.is_valid():
#            formset.save()
#            return HttpResponseRedirect("../success/")
#    else:
#        formset = BanqueFormSet(queryset=Banque.objects.none())
#    return render(request, "feuillesdetemps/add_banque.html", {"formset": formset,})

@permission_required('feuilles_de_temps.superviseur_eugenie')
def bloc_eugenie_approve(request):
    BlocFormSet = modelformset_factory(Bloc_Eugenie, form=BlocEugenieApproveFrom, extra=0)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                bloc = Bloc_Eugenie.objects.get(id=form.cleaned_data['id'].id)
                bloc.note = form.cleaned_data['note']
                bloc.approuve = form.cleaned_data['approuve']
                if bloc.approuve and bloc.banque:
                    employe = Employe.objects.get(id=form.cleaned_data['employe'].id)
                    if bloc.tache.type == 'PO':
                        employe.banque_heure += bloc.temps
                    else:
                        employe.banque_heure -= bloc.temps
                    employe.save()
                bloc.save()
            return HttpResponseRedirect("success/")
    else:
        employe = Employe.objects.get(user_id=request.user.id)
        formset = BlocFormSet(queryset=Bloc_Eugenie.objects.filter(employe__superviseur=employe, approuve=False).order_by('employe','date'))
    return render(request, "feuillesdetemps/bloc_eugenie_approve.html", {"formset": formset})


@login_required
def employe_edit_bloc_eugenie(request):
    BlocFormSet = modelformset_factory(Bloc_Eugenie, form=BlocEugenieEmployeForm, extra=0)
    employe = Employe.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                bloc = Bloc_Eugenie.objects.get(id=form.cleaned_data['id'].id)
                bloc.employe = employe
                bloc.date = form.cleaned_data['date']
                bloc.projet = form.cleaned_data['projet']
                bloc.tache = form.cleaned_data['tache']
                bloc.temps = form.cleaned_data['temps']
                bloc.note = form.cleaned_data['note']
                bloc.banque = form.cleaned_data['banque']
                bloc.approuve = False
                bloc.save()
            return HttpResponseRedirect("success/")
    else:
        formset = BlocFormSet(queryset=Bloc_Eugenie.objects.filter(employe=employe, approuve=False).order_by('date'))
    return render(request, "feuillesdetemps/employe_edit_bloc_eugenie.html", {"formset": formset})


@login_required
def employe_add_bloc_eugenie(request):
    BlocFormSet = modelformset_factory(Bloc_Eugenie, form=BlocEugenieEmployeForm)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                employe = Employe.objects.get(user_id=request.user.id)
                bloc = Bloc_Eugenie(
                    employe=employe,
                    date=form.cleaned_data['date'],
                    projet=form.cleaned_data['projet'],
                    tache=form.cleaned_data['tache'],
                    temps=form.cleaned_data['temps'],
                    note=form.cleaned_data['note'],
                    banque=form.cleaned_data['banque'],
                    approuve=False
                )
                bloc.save()
            return HttpResponseRedirect("success/")
    else:
        formset = BlocFormSet(queryset=Bloc_Eugenie.objects.none())
    return render(request,"feuillesdetemps/employe_add_bloc_eugenie.html", {"formset": formset})


@permission_required('feuilles_de_temps.superviseur_eugenie')
def view_banque(request):
    employes = Employe.objects.filter(user__is_active=True).exclude(banque_heure=0).order_by('compagnie', 'banque_heure')
    total = Employe.objects.filter(user__is_active=True).aggregate(total=Sum('banque_heure'))
    return render(request,"feuillesdetemps/view_banque.html",{"employes":employes,"total":total})