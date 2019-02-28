from django import forms
from gpao.models import *
from django.forms.formsets import formset_factory


class PieceSoumissionForm(forms.Form):
    choix = forms.BooleanField(required=False)
    piece = forms.ModelChoiceField(queryset=Piece.objects.all())
    qt = forms.IntegerField()

SoumissionFormset = formset_factory(PieceSoumissionForm, extra=0)