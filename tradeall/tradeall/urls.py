from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'profiles.views.home', name='home'),

    #profiles
    url(r'^profiles/', include('profiles.urls')),

    #admin
    url(r'^admin/', include(admin.site.urls)),
)
