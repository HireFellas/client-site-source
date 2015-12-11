from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from hirefellas import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hirefellas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^photologue/', include('photologue.urls')),
    url(r'^$', 'jobs.views.home'),
    url(r'^quote/', 'jobs.views.quoteForm'),
    url(r'^bids/', 'bids.views.listBids'),
    url(r'^contact/', 'jobs.views.contact'),
    url(r'^faq/', 'jobs.views.faq'),
    url(r'^terms/', 'jobs.views.terms'),
    url(r'^privacy/', 'jobs.views.privacy'),
    url(r'^team/', 'jobs.views.team'),
    url(r'^about/', 'jobs.views.about'),
    url(r'^success/', 'jobs.views.success'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes' : True }),

    )

urlpatterns += staticfiles_urlpatterns()
