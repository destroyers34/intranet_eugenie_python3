from django import forms
from projets.models import Projet_Eugenie


class DateRangeForm(forms.Form):
    date_debut = forms.DateField()
    date_fin = forms.DateField()


class FilterForm(forms.Form):
    date_debut = forms.DateField()
    date_fin = forms.DateField()
    projet = forms.ModelChoiceField(queryset=Projet_Eugenie.objects.all().order_by('numero'), empty_label=None)