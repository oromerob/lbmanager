from django.conf.urls import patterns, include, url as urlm
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'LB Manager'
admin.site.index_title = 'LB Manager'
admin.site.site_title = 'LB Manager'

urlpatterns = patterns('',
    urlm(r'^$', RedirectView.as_view(url='/admin')),
    urlm(r'^admin/', include(admin.site.urls)),
    urlm(r'^admin/balancer/custom/', include('apps.balancer.urls')),
    urlm(r'^admin/cluster/custom/', include('apps.cluster.urls')),
    urlm(r'^admin/nginx/custom/', include('apps.nginx.urls')),
    urlm(r'^admin/database/custom/', include('apps.config.urls')),
    urlm(r'^admin/config/custom/', include('apps.config.urls')),
    urlm(r'^status/', include('apps.status.urls')),
    urlm(r'^admin_tools/', include('admin_tools.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
