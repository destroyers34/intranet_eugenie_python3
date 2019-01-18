from django.contrib import admin
from ressources.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from ressources.forms import EmployeForm


class CompagnieAdmin(admin.ModelAdmin):
    list_display = ('nom','code')
    ordering = ('nom',)


class DeviseAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'code_iso', 'symbole', 'taux_toCAD', 'taux_inverse', 'date_taux')
    ordering       = ('nom', 'code_iso', )
    search_fields = ['nom', 'code_iso']


class TacheAdmin(admin.ModelAdmin):
    list_display = ('numero', 'description', 'type')
    search_fields = ['numero', 'description', 'type']


class CompteAdmin(admin.ModelAdmin):
    list_display   = ('numero', 'description', 'sens', 'devise', 'type', 'inactif')
    ordering       = ('numero',)
    search_fields = ['numero', 'description']
    exclude = ['employe']

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeInline(admin.TabularInline):
    model = Employe
    max_num = 1
    can_delete = False

class EmployeAdmin(admin.ModelAdmin):
    form = EmployeForm


# Define a new User admin
class UserAdmin(AuthUserAdmin):
    def compagnie(self, instance):
        return instance.employe.compagnie
    compagnie.short_description = 'Compagnie'

    def hire_date(self, instance):
        return instance.employe.hire_date
    hire_date.short_description = 'Date d\'embauche'

    def banque_heure(self, instance):
        return instance.employe.banque_heure
    banque_heure.short_description = 'Banque d\'heure'

    def taux_horaire(self, instance):
        return instance.employe.taux_horaire
    taux_horaire.short_description = 'Taux horaire'

    def superviseur(self, instance):
        return instance.employe.superviseur
    superviseur.short_description = 'Superviseur'

    ordering = ['-is_active', 'first_name', ]
    inlines = [EmployeInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'compagnie', 'banque_heure',
                    'hire_date', 'taux_horaire', 'superviseur', 'is_staff', 'is_active')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
        }),
    )

# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)
admin.site.register(Compagnie, CompagnieAdmin)
admin.site.register(Devise, DeviseAdmin)
admin.site.register(Tache, TacheAdmin)
admin.site.register(Compte_gl, CompteAdmin)
admin.site.register(Employe, EmployeAdmin)

