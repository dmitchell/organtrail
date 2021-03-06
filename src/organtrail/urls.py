from django.conf.urls import patterns, include, url
from organtrail.controller import organtrail

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'organtrail.views.home', name='home'),
    # url(r'^organtrail/', include('organtrail.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^organtrail/$', organtrail.home),
    url(r'^organtrail/recipient/(?P<provided_id>.*)$', organtrail.recipient),
    url(r'^organtrail/state/(?P<user_id>[^/]+)', organtrail.waiting_room),
    url(r'^organtrail/mechanics/(?P<user_id>[^/]+)/(?P<move_id>.+)$', organtrail.move)
)
