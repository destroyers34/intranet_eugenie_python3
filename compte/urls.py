from django.conf.urls import patterns, url
from views import *
from django.contrib.auth.decorators import permission_required, login_required

urlpatterns = patterns('compte.views',

    #url(r'^compte/$', 'view_fournisseurs_materiels', name='view_fournisseurs_materiels'),
    #url('^list/$', ListBlocksView.as_view(), name='depense-list'),
    #url('^depense/new$', CreateBlockView.as_view(), name='depense-new'),
    url(r'^depense-eci/(?P<pk>\d+)/$', login_required(EmployeEciDepenseEditView.as_view()), name='depense_eci_edit'),
    url(r'^depense-eci/new/$', login_required(EmployeEciDepenseCreateView.as_view()), name='depense_eci_create'),
    url(r'^depense-eci/list/$', login_required(EmployeEciDepenseListView.as_view()), name='depense_eci_list'),
    url(r'^depense-eci/delete/(?P<pk>[\w]+)/$', login_required(EmployeEciDepenseDeleteView.as_view()), name='depense_eci_delete'),
    url(r'^depense-eci/approve/$', permission_required('feuilles_de_temps.superviseur_eugenie')(AdminEciDepenseApprobation.as_view()), name='depense_eci_approve'),
    url(r'^depense-eci/(?P<pk>\d+)/(?P<year1>\d{4})-(?P<month1>\d{2})-(?P<day1>\d{2})/(?P<year2>\d{4})-(?P<month2>\d{2})-(?P<day2>\d{2})/$',
        login_required(AdminEciDepenseRapport.as_view(template_name='compte/rapport_depenseEci.html')), name='rapport_depense_eci'),
    url(r'^depense-eci/rapports/$', login_required(AdminEciDepenseRapportSelect.as_view()), name='rapport_depense_eci_select'),

    url(r'^depense-eci/(?P<pk>\d+)/(?P<year1>\d{4})-(?P<month1>\d{2})-(?P<day1>\d{2})/(?P<year2>\d{4})-(?P<month2>\d{2})-(?P<day2>\d{2})/print/$',
        login_required(AdminEciDepenseRapport.as_view(template_name='compte/Print_rapport_depenseEci.html')), name='rapport_depense_eci'),
    )