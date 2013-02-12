from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #Loggin
    (r'^login/$', 'auth.views.login_user'),
    #resultados
    (r'^resultados/$', 'JuegoApp.views.juegos'),
    (r'^resultados/(?P<pagina>\d+)/$', 'JuegoApp.views.juegos'),
    #apostar (Juegos)
    (r'^juegos/(?P<pagina>\d+)/(?P<idgame>\d+)/(?P<resa>\d+)/(?P<resb>\d+)/$', 'JuegoApp.views.juegosap'),
    (r'^juegos/$', 'JuegoApp.views.juegosap'),
    (r'^juegos/(?P<pagina>\d+)/$', 'JuegoApp.views.juegosap'),
    
    # Examples:
    # url(r'^$', 'scorecenter.views.home', name='home'),
    # url(r'^scorecenter/', include('scorecenter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Media
	(r'css/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_ROOT + 'templates/css'}),
	(r'images/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root': settings.STATIC_ROOT + 'templates/images'}),
	(r'js/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_ROOT + 'templates/js'}),
	(r'js/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': settings.STATIC_ROOT + 'templates/fonts'}),
)
