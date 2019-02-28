from django.conf.urls import patterns, url

urlpatterns = patterns('budget_materiel.views',

    url(r'^materiels/$', 'view_fournisseurs_materiels', name='view_fournisseurs_materiels'),
    url(r'^materiels/(?P<fournisseur_id>\d+)/$', 'fournisseurs_materiels_details', name='fournisseurs_materiels_details'),
    )