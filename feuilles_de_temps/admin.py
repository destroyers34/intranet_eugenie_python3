from django.contrib import admin
from feuilles_de_temps.models import Bloc_Eugenie, Bloc_TPE


class BlocEugenieAdmin(admin.ModelAdmin):
    list_display = ('employe', 'date', 'projet', 'tache', 'temps', 'note', 'banque', 'approuve')
    list_filter = ('employe', 'date', 'projet', 'tache')
    search_fields = ['employe__user__first_name', 'employe__user__last_name', 'projet__nom', 'projet__numero',
                     'tache__description', 'tache__numero']
    ordering = ('approuve', '-date',)


class BlocTPEAdmin(admin.ModelAdmin):
    list_display = ('employe', 'date', 'projet', 'tache', 'temps', 'note', 'banque', 'approuve')
    list_filter = ('employe', 'date', 'projet', 'tache')
    search_fields = ['employe__user__first_name', 'employe__user__last_name', 'projet__nom', 'projet__numero',
                     'tache__description', 'tache__numero']
    ordering = ('approuve', '-date',)


#class BanqueAdmin(admin.ModelAdmin):
#    list_display = ('employe', 'date', 'temps')
#    list_filter = ('employe','date')
#    search_fields = ['employe','date']
#    ordering = ('-date',)
    
admin.site.register(Bloc_TPE, BlocTPEAdmin)
admin.site.register(Bloc_Eugenie, BlocEugenieAdmin)
#admin.site.register(Banque, BanqueAdmin)

