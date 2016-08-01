from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lists, name = 'index'),
    url(r'^(?P<doc_id>[0-9]+)$/', views.detail, name = 'detail')   

]