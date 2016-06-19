from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cockbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^barkeeper/', include('barkeeper.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/barkeeper', permanent=True)),
)
