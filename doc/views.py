from django.shortcuts import render
from django.http import HttpResponse
from .models import Doc, Client

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

    num = Doc.objects.get(pk=doc_id).number

    if num < 10:
        num = "00" + str(num)
    elif num < 100:
        num = "0" + str(num)
    else:
        num = str(num)

    return render(request, 'doc/detail.html', {'doc': doc, 'num': num})