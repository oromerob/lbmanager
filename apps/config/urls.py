from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^sync$', views.sync, name='sync'),
	url(r'^database_status$', views.database_status, name='database_status'),
	url(r'^database_status_all$', views.database_status_all, name='database_status_all'),
	url(r'^health$', views.health, name='health'),
	url(r'^backend_disable/(?P<backend_name>\w+)/$', views.backend_disable, name='backend_disable'),
	url(r'^backend_enable/(?P<backend_name>\w+)/$', views.backend_enable, name='backend_enable'),
	url(r'^configuration_map$', views.configuration_map, name='configuration_map'),
]
