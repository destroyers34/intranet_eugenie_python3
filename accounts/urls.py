from django.conf.urls import *
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',

      #override the default urls
      url(r'^password_change/$',
                    auth_views.password_change,{'template_name': 'accounts/password_change_form.html'},
                    name='password_change'),

      url(r'^password_change_done/$',
                    auth_views.password_change_done,{'template_name': 'accounts/password_change_done.html'},
                    name='password_change_done'),

      url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}
                    ),

      url(r'^logout/$', 'django.contrib.auth.views.logout',{'template_name': 'accounts/logged_out.html'}
                    ),

      #and now add the registration urls
      url(r'', include('registration.backends.default.urls')),
)