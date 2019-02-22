from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.report, name='report'),
    url(r'^report/(?P<uch_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^report/sep_points/(?P<uch_id>[0-9]+)/$', views.sep_points, name='sep_points'),
    url(r'^report/ctgs_types_train/(?P<uch_id>[0-9]+)/$', views.ctgs_types_train, name='ctgs_types_train'),
    url(r'^report/speed_limits/(?P<uch_id>[0-9]+)/$', views.speed_limits, name='speed_limits'),

    url(r'^report/(?P<uch_id>[0-9]+)/save_uch/$', views.save_uch, name='save_uch'),
    url(r'^new_uch/$', views.new_uch_click, name='new_uch'),
    url(r'^create_uch/$', views.create_uch, name='create_uch'),
    url(r'^audit/$', views.auditPage, name='audit'),
    url(r'^api/(?P<KodDor>[0-9]+)/(?P<KodUch>[0-9]+)/(?P<fields>[A-Za-z0-9_\+]+)/$', views.api_track, name='api_track'),
    ]
