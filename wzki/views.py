from django.shortcuts import render

from models import DocList


# Create your views here.

def raz(request):
	all_doc = DocList.objects.all()
	return render(request, 'doc/index.html', {'all_doc' : all_doc})

