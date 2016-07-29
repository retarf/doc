from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    
    # /music/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^(?P<dokument_id>[0-9]+)/$', views.detail, name = 'detail'),
]