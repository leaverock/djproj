from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^report$', views.report, name='report'),
    url(r'^report/(?P<locomot_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^report/main_spec_resist_move/(?P<locomot_id>[0-9]+)/$', views.main_spec_resist_move, name='main_spec_resist_move'),
    url(r'^report/tract_mod/(?P<locomot_id>[0-9]+)/$', views.tract_mod, name='tract_mod'),
    url(r'^report/tract_mod/xap/(?P<xap_id>[0-9]+)/$', views.tract_mod_xap, name='tract_mod_xap'),
    url(r'^report/regenerat_braking/(?P<locomot_id>[0-9]+)/$', views.regenerat_braking, name='regenerat_braking'),
    url(r'^report/regenerat_braking/xap/(?P<xap_id>[0-9]+)/$', views.regenerat_braking_xap, name='regenerat_braking_xap'),
    url(r'^report/therm_engine/(?P<locomot_id>[0-9]+)/$', views.therm_engine, name='therm_engine'),
]
