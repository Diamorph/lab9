from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    url(r'^rest/add/$', views.rest, name = 'main'),
    url(r'^$', views.rest_get, name = 'main'),
    url(r'^rest/(\d+)/$', views.Restaurant_id, name = 'main'),
    url(r'^rest/del/(\d+)/$',views.DelRestaurant, name = 'main'),
    url(r'^users/$',views.show_user , name = 'main'),
    url(r'^rest/search/$',views.search, name = 'main'),
    url(r'^page',views.rest_get_user,name = 'main'),
]