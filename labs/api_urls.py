from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import api_views


urlpatterns = [
    url(r'^add/$', api_views.add),
    url(r'^$', api_views.rest_get),
    url(r'^del/(\d+)/$',api_views.delete),
]