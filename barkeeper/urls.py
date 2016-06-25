from django.conf.urls import patterns, url

from barkeeper import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/start$', views.start, name='start'),
    url(r'^admin/$', views.PumpsIndexView.as_view(), name='pumpIndex'),
    url(r'^admin/clean/$', views.clean, name='clean'),
    
)