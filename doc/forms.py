from django import forms

from django.forms import ModelForm

from doc.models import Doc


class Adddoc(ModelForm):
    class Meta:
        model = Doc
        ocalized_fields = ('__all___',)
        fields = [ 'doctype', 'number', 'date', 'client' ]