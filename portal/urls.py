from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^submit_form/$', views.submitted, name='submitted'),
=======
>>>>>>> 4b41014ffa5a96777832df9033e6ee6eb3a41994
)
