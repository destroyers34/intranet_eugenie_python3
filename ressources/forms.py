from django import forms
from ressources.models import *


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"

    compte_gl = forms.ModelMultipleChoiceField(queryset=Compte_gl.objects.filter(type='0'))

    def __init__(self, *args, **kwargs):
        super(EmployeForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['compte_gl'].initial = self.instance.compte_gl_set.all()

    def save(self, *args, **kwargs):
        # NOTE: Previously assigned Foos are silently reset
        instance = super(EmployeForm, self).save(commit=False)
        self.fields['compte_gl'].initial.update(employe=None)
        self.cleaned_data['compte_gl'].update(employe=instance)
        return instance

