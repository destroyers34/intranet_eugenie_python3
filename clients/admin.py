from django.contrib import admin
from clients.models import Compagnie, Contact

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1

class CompagnieAdmin(admin.ModelAdmin):
    list_display = ('nom','adresse','ville','province_etat','postal_code','pays','telephonne','fax')
    list_filter = ('ville','province_etat','pays')
    search_fields = ['nom','adresse','ville','province_etat','postal_code','pays','telephonne','fax']
    ordering = ('nom',)
    inlines = [
        ContactInline,
    ]

class ContactAdmin(admin.ModelAdmin):
    list_display = ('prenom','nom','fonction','telephonne','email')
    list_filter = ('compagnie','fonction')
    search_fields = ['prenom','nom','fonction','telephonne','email','compagnie']
    ordering = ('prenom','nom')
    
admin.site.register(Compagnie,CompagnieAdmin)
admin.site.register(Contact,ContactAdmin)


