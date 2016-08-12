from django.shortcuts import render
from django.http import HttpResponse
from .models import Doc, Client, Product
from .forms import Adddoc
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

all_doc = Doc.objects.order_by('number').all()
all_clients = Client.objects.order_by('code').all()
all_products = Product.objects.order_by('name').all()


### General section ###

def index(request):
    return render(request, 'doc/index.html', {'all_doc': all_doc, 'all_clients': all_clients})

### Documents section ###

def documents(request):
    return render(request, 'doc/doc/documents.html', { 'all_doc': all_doc })

def DocumentDetail(request, doc_id):
    try:
        doc = Doc.objects.get(pk=doc_id)
    except Doc.DoesNotExist:
        raise Http404("Document does not exist")

    return render(request, 'doc/doc/detail.html', {'doc': doc})

class DocCreate(CreateView):
    model = Doc
    fields = ['doctype', 'number', 'date', 'client' ]

### Clients section ###


def clients(request):
    return render(request, 'doc/client/clients.html', { 'all_clients': all_clients })

def ClientDetail(request, cli_id):
    try:
        client = Client.objects.get(pk=cli_id)
    except Client.DoesNotExist:
        raise Http404("Client does not exist")

    return render(request, 'doc/client/client_detail.html', { 'client': client })

### Products section

def products(request):
    return render(request, 'doc/products/products.html', { 'all_products': all_products })

def productDetail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return render(request, 'doc/products/product_detail.html', { 'product': product })




