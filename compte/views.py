from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from compte.forms import *
from compte.models import *
from django.db.models import Sum
import datetime
from django.shortcuts import render
from django.forms.models import modelformset_factory


#class ListBlocksView(ListView):

#    model = models.Depense


#class CreateBlockView(CreateView):
 #   model = models.Depense
  #  fields = '__all__'
   # def get_success_url(self):

    #    return reverse('depense-list')


#class EditBuildingsView(UpdateView):
 #   model = models.Depense
  #  fields = '__all__'
   # def get_template_names(self):
#
 #       return ['compte/facture_form.html']

  #  def get_form_class(self):

   #     return nested_formset_factory(
    #        models.Depense,
     #       models.Facture,
      #      models.Frais
       # )

 #   def get_success_url(self):

  #      return reverse('depense-list')
class DepenseEciMixin(object):
  def get_context_data(self, **kwargs):
    context = super(DepenseEciMixin, self).get_context_data(**kwargs)
    context['user'] = self.request.user
    return context


class EmployeEciDepenseListView(DepenseEciMixin, ListView):
    template_name = 'compte/EmployeEciDepenseList.html'
    model = Depense_Eci

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Depense_Eci.objects.filter(employe=self.request.user.employe).order_by('-date')
        return super(EmployeEciDepenseListView, self).get_context_data(**kwargs)



class EmployeEciDepenseCreateView(DepenseEciMixin, CreateView):
    template_name = 'compte/EmployeEciDepenseEdit.html'
    form_class = EmployeECIDepenseForm()
    success_url = reverse_lazy('depense_eci_list')
    model = Depense_Eci

    def form_valid(self, form):
        context = self.get_context_data()
        depense = form.save(commit=False)
        depense.employe = context['user'].employe
        depense.approuve = False
        depense.paye = False
        depense.save()
        return super(EmployeEciDepenseCreateView, self).form_valid(form)

    def get_form(self, form_class=EmployeECIDepenseForm):
     form = super(EmployeEciDepenseCreateView, self).get_form(EmployeECIDepenseForm)
     form.fields['gl'].queryset = self.request.user.employe.compte_gl_set.all()
     return form


class EmployeEciDepenseEditView(DepenseEciMixin, UpdateView):
    template_name = 'compte/EmployeEciDepenseEdit.html'
    form_class = EmployeECIDepenseForm
    success_url = reverse_lazy('depense_eci_list')
    model = Depense_Eci

    def form_valid(self, form):
        context = self.get_context_data()
        depense = form.save(commit=False)
        depense.employe = context['user'].employe
        depense.approuve = False
        depense.paye = False
        depense.save()
        return super(EmployeEciDepenseEditView, self).form_valid(form)

class EmployeEciDepenseDeleteView(DepenseEciMixin, DeleteView):
    model = Depense_Eci
    success_url=reverse_lazy('depense_eci_list')

    def get_queryset(self):
        qs = super(EmployeEciDepenseDeleteView, self).get_queryset()
        return qs.filter(employe=self.request.user.employe)


class AdminEciDepenseApprobation(DepenseEciMixin, View):
    form_class = AdminECIDepenseApprobationForm
    template_name = 'compte/AdminEciDepenseApprobation.html'

    def get(self, request, *args, **kwargs):
        employe = Employe.objects.get(user_id=request.user.id)
        DepenseFormset = modelformset_factory(Depense_Eci, form=AdminECIDepenseApprobationForm, extra=0)
        formset = DepenseFormset(queryset=Depense_Eci.objects.filter(employe__superviseur=employe).order_by('employe','date'))
        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        DepenseFormset = modelformset_factory(Depense_Eci, form=AdminECIDepenseApprobationForm, extra=0)
        formset = DepenseFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                depense = Depense_Eci.objects.get(id=form.cleaned_data['id'].id)
                if depense.paye:
                    pass
                else:
                    if form.cleaned_data['approuve'] != None:
                        depense.approuve = form.cleaned_data['approuve']
                    if depense.approuve == True:
                        depense.paye = form.cleaned_data['paye']
                        depense.approved_by = request.user.employe
                        depense.approved_on = datetime.datetime.now()
                    if depense.approuve == False:
                        depense.paye = False
                        depense.approved_by = None
                        depense.approved_on = None
                depense.save()
            return HttpResponseRedirect('/compte/depense-eci/approve')

        return render(request, self.template_name, {'formset': formset})


class AdminEciDepenseRapport(DepenseEciMixin, ListView):
    model = Depense_Eci

    def get_queryset(self):
        date1 = datetime.date(int(self.kwargs.get('year1')),int(self.kwargs.get('month1')),int(self.kwargs.get('day1')))
        date2 = datetime.date(int(self.kwargs.get('year2')),int(self.kwargs.get('month2')),int(self.kwargs.get('day2')))
        qs = Depense_Eci.objects.filter(employe=self.kwargs['pk'],date__range=[date1, date2]).order_by('gl')
        return qs

    def get_context_data(self, **kwargs):
        context = super(AdminEciDepenseRapport, self).get_context_data(**kwargs)
        context['date1'] = datetime.date(int(self.kwargs.get('year1')),int(self.kwargs.get('month1')),int(self.kwargs.get('day1')))
        context['date2'] = datetime.date(int(self.kwargs.get('year2')),int(self.kwargs.get('month2')),int(self.kwargs.get('day2')))
        context['total'] = Depense_Eci.objects.filter(employe=self.kwargs['pk']).aggregate(total=Sum('montant')+Sum('tvq')+Sum('tps'), t_tvq=Sum('tvq'), t_tps=Sum('tps'))
        context['subtotal'] = Depense_Eci.objects.filter(employe=self.kwargs['pk'],date__range=[context['date1'], context['date2']]).values('gl__numero','gl__description').annotate(subtotal=Sum('montant')).order_by('gl__numero')
        return context


class AdminEciDepenseRapportSelect(DepenseEciMixin, View):
    form_class = AdminECIDepenseRapportForm
    template_name = 'compte/AdminEciDepenseRapportSelect.html'

    def get(self, request, *args, **kwargs):
        form = AdminECIDepenseRapportForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AdminECIDepenseRapportForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('/compte/depense-eci/' + str(form.cleaned_data['employe'].id) + '/' + str(form.cleaned_data['date']) + '/' + str(form.cleaned_data['date_fin']))

        return render(request, self.template_name, {'form': form})