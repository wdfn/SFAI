from django.conf.urls import patterns, url

from sfai import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
