from django.shortcuts import render
from .models import DocList, Clients

# Create your views here.

def lists(request):
	all_doc = DocList.objects.order_by('number').all()
	all_clients = Clients.objects.all()
	return render(request, 'doc/index.html', 
		{'all_doc' : all_doc, 
		'all_clients' : all_clients,
		})

def detail(request, doc_id):
	return render(request, "<h1> Szczegoly dla " + doc_id + " <h1>")


