from django.contrib import admin
from listes_de_prix.models import Option, Machine, Fournisseur, Categorie


class MachinerieInline(admin.TabularInline):
    model = Option.machines.through
    extra = 1


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nom_en')
    search_fields = ['nom', 'nom_en']
    ordering       = ('nom', )


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephonne', 'fax', 'siteweb', 'devise', 'ratio', 'ratio_us', 'actif')
    list_filter = ('devise',)
    ordering = ('-actif', 'nom',)


class MachineAdmin(admin.ModelAdmin):
    list_display   = ('numero', 'description', 'short_details', 'categorie', 'fournisseur', 'prix_fournisseur', 'prixCAD_f',
                      'dateprix', 'escompte', 'costCAD_f', 'ratioEffectif', 'pl_f', 'ratioEffectifUs', 'plUS_f',
                      'profit_f', 'profitUS_f', 'profit_pourcent_f', 'profitUS_pourcent_f', 'actif')
    search_fields = ['numero', 'description']
    list_filter    = ('categorie', 'fournisseur')
    ordering       = ('-actif', '-categorie', 'numero')
    fields = (('numero', 'description', 'categorie'), 'details', 'details_en',
              ('fournisseur', 'prix_fournisseur', 'dateprix'), ('escompte', 'ratio', 'ratio_us'), 'actif')
    inlines = [
        MachinerieInline,
    ]

    def short_details(self, obj):
        if obj.details:
            if len(obj.details) > 15:
                return obj.details[0:15] + '...'
            else:
                return obj.details
        else:
            return '-'
    short_details.short_description = 'Détails'

    def prixCAD_f(self, obj):
        return "%.2f" % obj.prixCAD()
    prixCAD_f.short_description = 'Prix ($CA)'

    def costCAD_f(self, obj):
        return "%.2f" % obj.cost()
    costCAD_f.short_description = 'Cost ($CA)'

    def pl_f(self, obj):
        return "%.2f" % obj.plMin()
    pl_f.short_description = 'PL ($CA)'

    def plUS_f(self, obj):
        return "%.2f" % obj.plMinUS()
    plUS_f.short_description = 'PL (US$)'

    def profit_f(self, obj):
        return "%.2f" % obj.profit()
    profit_f.short_description = 'Profit ($CA)'

    def profit_pourcent_f(self, obj):
        return "%.2f" % obj.profit_pourcent()
    profit_pourcent_f.short_description = 'Profit (% Brute)'

    def profitUS_f(self, obj):
        return "%.2f" % obj.profitUs()
    profitUS_f.short_description = 'Profit US ($CA)'

    def profitUS_pourcent_f(self, obj):
        return "%.2f" % obj.profit_pourcentUs()
    profitUS_pourcent_f.short_description = 'Profit US (% Brute)'


class OptionAdmin(admin.ModelAdmin):
    actions = None
    list_display   = ('numero', 'short_details', 'fournisseur', 'prix_fournisseur', 'prixCAD_f', 'dateprix', 'escompte',
                      'costCAD_f', 'ratioEffectif', 'pl_f', 'profit_f', 'profit_pourcent_f')
    search_fields = ['numero', 'description']
    list_filter    = ('fournisseur',)
    ordering       = ('numero', )
    fields = ('numero', 'details', 'details_en',
              ('fournisseur', 'prix_fournisseur', 'dateprix'), ('escompte', 'ratio', 'ratio_us'))
    inlines = [
        MachinerieInline,
    ]
    exclude = ('machines',)

    def short_details(self, obj):
        if obj.details:
            if len(obj.details) > 50:
                return obj.details[0:50] + '...'
            else:
                return obj.details
        else:
            return '-'
    short_details.short_description = 'Détails'

    def prixCAD_f(self, obj):
        return "%.2f" % obj.prixCAD()
    prixCAD_f.short_description = 'Prix ($CA)'

    def costCAD_f(self, obj):
        return "%.2f" % obj.cost()
    costCAD_f.short_description = 'Cost ($CA)'

    def pl_f(self, obj):
        return "%.2f" % obj.plMin()
    pl_f.short_description = 'PL ($CA)'

    def profit_f(self, obj):
        return "%.2f" % obj.profit()
    profit_f.short_description = 'Profit ($CA)'

    def profit_pourcent_f(self, obj):
        return "%.2f" % obj.profit_pourcent()
    profit_pourcent_f.short_description = 'Profit (% Brute)'

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)