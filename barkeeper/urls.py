from django.conf.urls import patterns, url

from barkeeper import views
from cockbot.urls import urlpatterns

urlpatterns = patterns('' ,
    url(r'^$', views.index, name='index'),
)