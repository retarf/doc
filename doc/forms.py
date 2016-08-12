from django import forms

from django.forms import ModelForm

from doc.models import Doc, Client


class Adddoc(ModelForm):
    class Meta:
        model = Doc
        localized_fields = ('__all___',)
        fields = [ 'doctype', 'number', 'date', 'client' ]

class AddCli(ModelForm):
    class Meta:
        model = Client
        localized_fields = ('__all__')
        fields = [ 'code', 'name', 'nip', 'street', 'number', 'city', 'zip_number' ]























