from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^report/$', views.report, name='report'),
    url(r'^report/(?P<uch_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^report/sep_points/(?P<uch_id>[0-9]+)/$', views.sep_points, name='sep_points'),
    url(r'^report/ctgs_types_train/(?P<uch_id>[0-9]+)/$', views.ctgs_types_train, name='ctgs_types_train'),
    url(r'^report/speed_limits/(?P<uch_id>[0-9]+)/$', views.speed_limits, name='speed_limits'),

    url(r'^report/(?P<uch_id>[0-9]+)/save_uch/$', views.save_uch, name='save_uch'),
    ]
