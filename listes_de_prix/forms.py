from django import forms
from django.forms.models import BaseModelFormSet
from django.contrib.auth.models import User
from listes_de_prix.models import Option


class OptionForm(forms.ModelForm):
    calcul = forms.BooleanField(required=False)
        
    class Meta:
        model = Option
        exclude = ('ratio', 'fournisseur', 'escompte', 'description', 'details', 'prix_fournisseur', 'dateprix',
                   'machines', 'description_en', 'details_en', 'ratio_us')
    
    def __init__(self, *args, **kwargs):
        super(OptionForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['numero'].widget.attrs['readonly'] = True


class BaseOptionFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseOptionFormSet, self).__init__(*args, **kwargs)