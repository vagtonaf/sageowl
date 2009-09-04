from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dja/', include('dja.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^questoes/$', 'sageowl.questoes.views.index'),
    (r'^questoes/(?P<questao_id>\d+)/$', 'sageowl.questoes.views.detail'),
    (r'^questoes/(?P<questao_id>\d+)/resultado/$', 'sageowl.questoes.views.resultado'),
    (r'^questoes/(?P<questao_id>\d+)/cadastro/$', 'sageowl.questoes.views.cadastro'),

    (r'^admin/(.*)', admin.site.root),
         
)
