from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Doc, Client, Product, income
from .forms import Adddoc, IncomeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

all_doc = Doc.objects.order_by('number').all().reverse()
all_clients = Client.objects.order_by('code').all()
all_products = Product.objects.order_by('name').all()


### General section ###

def index(request):
    return render(request, 'doc/index.html', {'all_doc': all_doc, 'all_clients': all_clients})

### Documents section ###

def documents(request):
    return render(request, 'doc/doc/documents.html', { 'all_doc': all_doc })

def all_inc_func(doc_id):
    all_inc = income.objects.filter(docum_id=doc_id)

    return {'all_inc': all_inc}


def doc_calculation(doc_id):

    all_inc = income.objects.filter(docum_id=doc_id)

    # quantity sum calculation (var q)
    q = 0

    for i in all_inc:
        q = q + i.quantity

    # valume sum calculation (var v)
    v = 0

    return {'q': q, 'v': v}


def DocumentDetail(request, doc_id):

    try:
        doc = Doc.objects.get(pk=doc_id)
        q = doc_calculation(doc_id).q
        v = doc_calculation(doc_id).v

    except Doc.DoesNotExist:
        raise Http404("Document does not exist")

    return render(request, 'doc/doc/detail.html', {'doc': doc, 'all_inc': all_inc, 'quantity_sum': q, 'valume_sum': v, 'dec': dec, 'inc': inc})

'''
    #if not doc.DoesNotExist:

    else:

        q = doc_calculation(doc_id).q
        v = doc_calculation(doc_id).v

        # calkulation for "poprzedni" and "nastepny" button

        doc_id = int(doc_id)

        dec = doc_id - 1

        try:
            dec = Doc.objects.get(pk = dec)
        except Doc.DoesNotExist:
            dec = Doc.objects.order_by('id').first()

        inc = doc_id + 1

        try:
            inc = Doc.objects.get(pk = inc)
        except Doc.DoesNotExist:
            if Doc.objects.order_by('id').last().id == doc_id:
                inc = Doc.objects.order_by('id').last()
            else:
                try:
                    inc = inc + 1
                except inc >= doc_id:
                    pass


'''

class DocCreate(CreateView):
    model = Doc
    fields = ['doctype', 'number', 'date', 'client' ]



    def idreturn(self):
        doc_id = self.id
        return doc_id

class incomeCreate(CreateView):
    model = income
    fields = ['docum', 'product', 'quantity', 'price', 'value']

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

