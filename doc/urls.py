from django.conf.urls import url
from . import views


app_name = 'doc'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),

    ### Documents section ###
    # /doc/71/
    url(r'^doc/(?P<doc_id>[0-9]+)/$', views.DocumentDetail, name = 'DocumentDetail'),
    url(r'^doc/$', views.documents, name = 'documents'),
    # add_doc
    # url(r'^doc/add/$', views.DocCreate.as_view(), name = 'doc-add'),
    url(r'^doc/income_form/$', views.incomeCreate.as_view(), name = 'income_form'),
    url(r'^doc_form/$', views.DocCreate.as_view(), name = 'doc-add'),

    ### Clients section ###
    url(r'^client/$', views.clients, name = 'clients'),
    url(r'^client/(?P<cli_id>[0-9]+)/$', views.ClientDetail, name = 'ClientDetail'),

    ### Products section ###

    url(r'^products/$', views.products, name='products'),
url(r'^products/(?P<product_id>[0-9]+)/$', views.productDetail, name = 'productDetail'),
]