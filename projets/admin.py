from django.contrib import admin
from projets.models import Projet_Eugenie, Projet_TPE


class ProjetEugnieAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nom', 'modele', 'serial_number', 'budget_mat', 'budget_mo', 'client', 'date_soumission',
                    'date_debut', 'date_fin', 'actif', 'en_attente', 'priority')
    list_filter = ('nom', 'modele', 'date_soumission', 'date_debut', 'date_fin', 'priority')
    ordering = ('-en_attente', '-actif', 'priority', '-numero')
    raw_id_fields = ('client',)
    fields = ('numero', ('nom', 'modele'), 'serial_number', ('budget_mat', 'budget_mo'), 'client',
              ('date_soumission', 'date_debut', 'date_fin'), ('en_attente', 'actif', 'priority'))


class ProjetTPEAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nom', 'description', 'serial_number', 'budget_mat', 'budget_mo', 'client',
                    'date_soumission', 'date_debut', 'date_fin', 'actif', 'en_attente')
    list_filter = ('nom', 'date_soumission', 'date_debut', 'date_fin')
    ordering = ('-actif', '-numero',)
    raw_id_fields = ('client',)
    fields = (('numero', 'nom'), 'description', 'serial_number', ('budget_mat', 'budget_mo'), 'client',
              ('date_soumission', 'date_debut', 'date_fin'), ('en_attente', 'actif'))
    
admin.site.register(Projet_Eugenie, ProjetEugnieAdmin)
admin.site.register(Projet_TPE, ProjetTPEAdmin)


