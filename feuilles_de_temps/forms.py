from django import forms
from feuilles_de_temps.models import Bloc_Eugenie, Banque, Bloc_TPE
from projets.models import Projet_Eugenie, Projet_TPE
from ressources.models import Employe


class BlocEugenieForm(forms.ModelForm):
    projet = forms.ModelChoiceField(queryset=Projet_Eugenie.objects.order_by('-actif', '-numero'))
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))

    class Meta:
        model = Bloc_Eugenie
        fields = '__all__'


class BlocEugenieEmployeForm(forms.ModelForm):
    projet = forms.ModelChoiceField(queryset=Projet_Eugenie.objects.filter(actif=True).order_by('-numero'))

    class Meta:
        model = Bloc_Eugenie
        exclude = ['employe', 'approuve']

    def __init__(self, *arg, **kwarg):
        super(BlocEugenieEmployeForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False


class BlocEugenieApproveFrom(forms.ModelForm):
    class Meta:
        model = Bloc_Eugenie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BlocEugenieApproveFrom, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['date'].widget.attrs['readonly'] = True
            self.fields['projet'].widget.attrs['readonly'] = True
            self.fields['tache'].widget.attrs['readonly'] = True
            self.fields['temps'].widget.attrs['readonly'] = True

    def clean_date(self):
        return self.instance.date

    def clean_projet(self):
        return self.instance.projet

    def clean_tache(self):
        return self.instance.tache

    def clean_temps(self):
        return self.instance.temps


class BanqueForm(forms.ModelForm):
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))

    class Meta:
        model = Banque
        fields = '__all__'


class BlocTPEForm(forms.ModelForm):
    projet = forms.ModelChoiceField(queryset=Projet_TPE.objects.order_by('-actif','-numero'))
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))

    class Meta:
        model = Bloc_TPE
        fields = '__all__'


class ConsultationBlocEugenieForm(forms.ModelForm):
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))
    date_debut = forms.DateField()
    date_fin = forms.DateField()

    class Meta:
        model = Bloc_Eugenie
        fields = ['employe', 'date_debut', 'date_fin']


class ConsultationBlocTPEForm(forms.ModelForm):
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))
    date_debut = forms.DateField()
    date_fin = forms.DateField()

    class Meta:
        model = Bloc_TPE
        fields = ['employe', 'date_debut', 'date_fin']