from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uchastk/$', views.uch_index, name='uch_index'),
    url(r'^uchastk/razdel_punkt/$', views.razdel_punkt, name='razdel_punkt'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + staticfiles_urlpatterns()