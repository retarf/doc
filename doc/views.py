from django.shortcuts import render
from django.http import HttpResponse
from .models import Doc, Client

# Create your views here.

def lists(request):
 all_doc = Doc.objects.order_by('number').all()
 all_clients = Client.objects.all()
 return render(request, 'doc/index.html',
  {'all_doc' : all_doc,
  'all_clients' : all_clients,
  })

def detail(request, doc_id):
 return HttpResponse("<h1> Szczegoly dla " + str(doc_id) + " <h1>")