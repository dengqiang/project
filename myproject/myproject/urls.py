from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
from tn.views import *
from users.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^UserRegister/$',UserRegister),
#    url(r'^css/(?P<path>.*)$','django.views.static.serve',  
 #                        {'document_root':settings.TEMPLATE_DIRS[0]+'/css'}),
  #  url(r'^pic/(?P<path>.*)$','django.views.static.serve',  
   #                         {'document_root':settings.TEMPLATE_DIRS[0]+'/pic'}),  
#    url(r'^js/(?P<path>.*)$','django.views.static.serve',  
 #                           {'document_root':settings.TEMPLATE_DIRS[0]+'/js'}),  
    url(r'^login/$',login),
    url(r'^main/$',main),
    url(r'^upload/$',uploadimg),
    
    url(r'^newtrip/$',newtrip),
)

