from django.contrib import admin
from budget_materiel.models import Materiel_Eugenie, Fournisseur, Categorie


class MaterielEugenieAdmin(admin.ModelAdmin):
    list_display = ('date', 'projet', 'fournisseur', 'categorie', 'montant')
    list_filter = ('date', 'projet', 'fournisseur', 'categorie')
    search_fields = ['projet__nom', 'projet__numero', 'fournisseur', 'categorie__nom']
    ordering = ('-date',)
    fields = ('date', 'projet', 'fournisseur', 'categorie', 'montant')


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    ordering = ('nom',)


admin.site.register(Materiel_Eugenie, MaterielEugenieAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Categorie)
