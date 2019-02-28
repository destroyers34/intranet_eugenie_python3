from django.contrib.admin import site, ModelAdmin
from .models import *


class Depense_EciAdmin(ModelAdmin):
    list_display = ('id', 'date', 'employe', 'detail', 'gl', 'projet', 'montant', 'tps', 'tvq', 'fac_total', 'photo', 'approuve', 'approved_by', 'approved_on', 'paye', )
    list_filter = ('employe', 'date', 'gl', 'projet')
    ordering = ('date', 'employe')

site.register(Depense_Eci, Depense_EciAdmin)

class Depense_TpeAdmin(ModelAdmin):
    list_display = ('id', 'date', 'employe', 'detail', 'gl', 'projet', 'montant', 'tps', 'tvq', 'fac_total', 'photo', 'approuve', 'approved_by', 'approved_on', 'paye', )
    list_filter = ('employe', 'date', 'gl', 'projet')
    ordering = ('date', 'employe')

site.register(Depense_Tpe, Depense_TpeAdmin)

class Pc_EciAdmin(ModelAdmin):
    list_display = ('date', 'employe', 'detail', 'gl', 'projet', 'montant', 'tps', 'tvq', 'fac_total')
    list_filter = ('employe', 'date', 'gl', 'projet')
    ordering = ('date',)

site.register(Petite_Caisse_Eci, Pc_EciAdmin)