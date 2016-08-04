from django.shortcuts import render
from django.http import HttpResponse
from .models import Doc, Client
from .forms import Adddoc
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

all_doc = Doc.objects.order_by('number').all()
all_clients = Client.objects.order_by('code').all()


def index(request):
    return render(request, 'doc/index.html', {'all_doc': all_doc, 'all_clients': all_clients})

    '''
    return render(request, 'doc/index.html', 
        {'html': html,
        })
    '''

def lists(request):
    return render(request, 'doc/index.html',
        {'all_doc' : all_doc,
        'all_clients' : all_clients,
        })

def detail(request, doc_id):
    try:
        doc = Doc.objects.get(pk=doc_id)
    except Doc.DoesNotExist:
        raise Http404("Document does not exist")

    return render(request, 'doc/detail.html', {'doc': doc})

class DocCreate(CreateView):
    model = Doc
    fields = ['doctype', 'number', 'date', 'client' ]
