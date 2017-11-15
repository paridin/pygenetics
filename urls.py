from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from execute import views as eview
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = (
    url(r'^$', views.index),
    url(r'^es/$', views.index),
    url(r'^en/$', views.index_us),
    url(r'^upload/?.*$', views.upload),
    url(r'^list_cnf/$', views.list_cnf),
    url(r'^upload_progress/?.*$', views.upload_progress),
    url(r'^test/$', views.test),
    url(r'^execute/run/$', eview.run),
    url(r'^execute/list_results/$', eview.list_results),
    url(r'^preview_cnf/$', views.get_cnf),
    url(r'^execute/save_log/$', eview.save_log),
    url(r'^execute/save_averages/$', eview.save_averages),
    # (r'^upload/','upload.upload')
    # Example:
    # (r'^web/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls,)),
)

if settings.DEBUG:
    urlpatterns += (
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
    )
