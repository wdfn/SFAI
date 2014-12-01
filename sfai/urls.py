from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfai.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^form_upload.html/', 'portal.views.uploadSubmission' )
    url(r'^admin/', include(admin.site.urls)),
)
