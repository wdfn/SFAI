from django.conf.urls import patterns, url

from sfai import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^submit_form/$', views.submitted, name='submitted'),
)
