from django.conf.urls import patterns, url
 
urlpatterns = patterns('gpao.views',
        url(r'^$', 'main_gpao', name='main_gpao'),
        url(r'^nm/$', 'liste_nm', name='liste_nm'),
        url(r'^nm/(?P<no_nm>NM-\d{4}-\d{2})/$', 'details_nm', name='details_nm'),
        url(r'^nm/(?P<no_nm>NM-\d{4}-\d{2})/soumission$', 'soumission', name='soumission'),
        url(r'^pe/$', 'liste_pe', name='liste_pe'),
        url(r'^piece/$', 'liste_piece', name='liste_piece'),
        url(r'^piece/(?P<no_piece>\w{3}-\d{4}-\d{2})/$', 'details_piece', name='details_piece'),
        url(r'^famille/$', 'liste_famille', name='liste_famille'),
        url(r'^famille/(?P<famille>\w{3})/$', 'famille_piece', name='famille_piece'),
    )