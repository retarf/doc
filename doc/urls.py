from django.conf.urls import url
from . import views


app_name = 'doc'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),

    # /doc/71/
    url(r'^(?P<doc_id>[0-9]+)/$', views.detail, name = 'detail'),

    # add_doc
    url(r'^add/$', views.DocCreate.as_view(), name = 'doc-add'),
]