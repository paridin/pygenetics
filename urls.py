from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^$','pyGenetics.views.index'),
     (r'^es/$','pyGenetics.views.index'),
     (r'^en/$','pyGenetics.views.index_us'),
     (r'^upload/?.*$','pyGenetics.views.upload'),
     (r'^upload_progress/?.*$','pyGenetics.views.upload_progress'),
     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'pyGenetics.settings.MEDIA_ROOT' , 'show_indexes':True}),
     (r'^list_cnf/$','pyGenetics.views.list_cnf'),
     (r'^test/$','pyGenetics.views.test'),
     (r'^execute/run/$','pyGenetics.execute.views.run'),
     (r'^execute/list_results/$','pyGenetics.execute.views.list_results'),
     (r'^preview_cnf/$','pyGenetics.views.get_cnf'),
     (r'^execute/save_log/$','pyGenetics.execute.views.save_log'),
     (r'^execute/save_averages/$','pyGenetics.execute.views.save_averages'),
    # (r'^upload/','pyGenetics.upload.upload')
    # Example:
    # (r'^web/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)

