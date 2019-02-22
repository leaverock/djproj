from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vivod/$', views.vivod, name='vivod'),
    url(r'^multiVar/$', views.multiVar, name='multiVar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + staticfiles_urlpatterns()
