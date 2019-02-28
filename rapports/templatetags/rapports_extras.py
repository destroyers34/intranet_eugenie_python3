__author__ = 'destroyers34'
from django import template
register = template.Library()


@register.filter(name='prod_pourcent')
def prod_pourcent(obj, arg):
    return obj.pourcent_tache(arg)

@register.filter(name='prod_heure')
def prod_heure(obj, arg):
    return obj.heure_tache(arg)