from django.conf.urls import patterns, url
 
urlpatterns = patterns('listes_de_prix.views',

    url(r'^fournisseurs/$', 'liste_fournisseurs', name='liste_fournisseurs'),
    url(r'^fournisseurs/(?P<fournisseur_id>\d+)/$', 'detail_fournisseur', name='detail_fournisseur'),
    url(r'^(?P<fournisseur_id>\d+)/$', 'liste_machines', name='liste_machines'),
    url(r'^(?P<fournisseur_id>\d+)/(?P<machine_id>\d+)$', 'details_machine', name='details_machine'),
    url(r'^print/(?P<fournisseur_id>\d+)/$', 'print_liste_machines', name='print_liste_machines'),

    url(r'^us/(?P<fournisseur_id>\d+)/$', 'liste_machines_en', name='liste_machines_en'),
    url(r'^us/(?P<fournisseur_id>\d+)/(?P<machine_id>\d+)$', 'details_machine_en', name='details_machine_en'),
    url(r'^print/us/(?P<fournisseur_id>\d+)/$', 'print_liste_machines_en', name='print_liste_machines_en'),
    )