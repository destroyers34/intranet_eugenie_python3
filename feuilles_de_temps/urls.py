from django.conf.urls import patterns, url
 
urlpatterns = patterns('feuilles_de_temps.views',

    url(r'^blocs/eci/$', 'blocs_eci', name='blocs_eci'),
    url(r'^blocs/tpe/$', 'blocs_tpe', name='blocs_tpe'),
    url(r'^blocs/eci/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$',
        'consultation_blocs_eci', name='consultation_blocs_eci'),
    url(r'^blocs/tpe/(?P<username>[A-Za-z]+)/(?P<date_debut>\d{4}-\d{2}-\d{2})/(?P<date_fin>\d{4}-\d{2}-\d{2})/$',
        'consultation_blocs_tpe', name='consultation_blocs_tpe'),
    url(r'^blocs/eci/add/$', 'add_blocs_eci', name='add_blocs_eci'),
    url(r'^blocs/eci/success/$', 'success', name='success'),
    url(r'^blocs/tpe/add/$', 'add_blocs_tpe', name='add_blocs_tpe'),
    url(r'^blocs/tpe/success/$', 'success', name='success'),
    url(r'^banque/$', 'view_banque', name='view_banque'),
    #url(r'^banque/success/$', 'success', name='success'),
    url(r'^employe/eci/add/$', 'employe_add_bloc_eugenie', name='employe_add_bloc_eugenie'),
    url(r'^employe/eci/edit/$', 'employe_edit_bloc_eugenie', name='employe_edit_bloc_eugenie'),
    url(r'^employe/eci/add/success/$', 'add_success', name='add_success'),
    url(r'^employe/eci/edit/success/$', 'edit_success', name='edit_success'),
    url(r'^employe/eci/approuve/$', 'bloc_eugenie_approve', name='bloc_eugenie_approve'),
    url(r'^employe/eci/approuve/success/$', 'edit_success', name='edit_success'),
    )