from django import forms
from compte.models import *
from ressources.models import Compte_gl
from django.forms.formsets import formset_factory


class EmployeECIDepenseForm(forms.ModelForm):
    gl = forms.ModelChoiceField(queryset=Compte_gl.objects.all())

    class Meta:
        model = Depense_Eci
        fields = ['date', 'detail', 'projet', 'gl', 'tps', 'tvq', 'montant', 'photo']
        exclude = ['employe', 'approuve', 'paye']

    def __init__(self, *args, **kwargs):
         #user = kwargs.pop('user')
         super(EmployeECIDepenseForm, self).__init__(*args, **kwargs)
         #self.fields['gl'].queryset = Compte_gl.objects.filter(user.employe__compte_gl)


class AdminECIDepenseRapportForm(forms.ModelForm):
    date_fin = forms.DateField(label='Date de fin')
    class Meta:
        model = Depense_Eci
        fields = ['date', 'employe']


class AdminECIDepenseApprobationForm(forms.ModelForm):
    class Meta:
        model = Depense_Eci
        exclude = ['approved_on', 'approved_by']

    def __init__(self, *args, **kwargs):
        super(AdminECIDepenseApprobationForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['employe'].widget.attrs['readonly'] = True
            self.fields['date'].widget.attrs['readonly'] = True
            self.fields['detail'].widget.attrs['readonly'] = True
            self.fields['projet'].widget.attrs['readonly'] = True
            self.fields['gl'].widget.attrs['readonly'] = True
            self.fields['montant'].widget.attrs['readonly'] = True
            self.fields['tps'].widget.attrs['readonly'] = True
            self.fields['tvq'].widget.attrs['readonly'] = True
            self.fields['photo'].widget.attrs['readonly'] = True

    def clean_date(self):
        return self.instance.date

    def clean_projet(self):
        return self.instance.projet

    def clean_employe(self):
        return self.instance.employe

    def clean_detail(self):
        return self.instance.detail

    def clean_gl(self):
        return self.instance.gl

    def clean_montant(self):
        return self.instance.montant

    def clean_tps(self):
        return self.instance.tps

    def clean_tvq(self):
        return self.instance.tvq

    def clean_photo(self):
        return self.instance.photo