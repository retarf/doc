from django import forms

from django.forms import ModelForm

from doc.models import Doc, Client, income


class Adddoc(ModelForm):
    class Meta:
        model = Doc
        fields = [ 'doctype', 'number', 'date', 'client' ]

class AddCli(ModelForm):
    class Meta:
        model = Client
        fields = [ 'code', 'name', 'nip', 'street', 'number', 'city', 'zip_number' ]

class IncomeForm(ModelForm):
    class Meta:
        model = income
        fields = ['docum', 'product', 'quantity', 'price', 'value']

        def docum_id(doc_id):
            docum = doc_id



