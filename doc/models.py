from __future__ import unicode_literals

from django.db import models

from django.db.models import CharField, IntegerField, BooleanField, ForeignKey, FloatField, DateField

from datetime import date

from django.forms import ModelForm

from django.core.urlresolvers import reverse

# Create your models here.

class Client(models.Model):
    code = CharField(max_length=50)
    name = CharField(max_length=100)
    nip = CharField(max_length=10)
    street = CharField(max_length=100)
    number = IntegerField()
    city = CharField(max_length=50)
    zip_number = CharField(max_length=5)

    def get_absolute_url(self):
        return reverse('doc:clidetail', kwargs={ 'cli_id': self.id })

    def __str__(self):
        return "  " + self.code + " " + self.name + " " + self.nip + " " + self.zip_number + " " + self.city + " " + self.street + " " + str(self.number)

class Product(models.Model):
    itswine = BooleanField(default=True)
    name = CharField(max_length=50)
    year = CharField(max_length=4)
    color = CharField(max_length=15)
    dryness = CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.year + " " + self.color + " " + self.dryness

def getNumber():
    doc = Doc.objects.order_by('number').last().number + 1
    return doc


class Doc(models.Model):

    WZ = 'WZ'
    PZ = 'PZ'
    RW = 'RW'
    PW = 'PW'

    DOC_TYPE_CHOICES=(
        (WZ, 'WZ'),
        (PZ, 'PZ'),
        (RW, 'RW'),
        (PW, 'PW'),
    )

    doctype = models.CharField(
        max_length=2,
        choices=DOC_TYPE_CHOICES,
        default=WZ,
    )

    number = IntegerField()

    date = DateField(default=date.today)

    number=IntegerField(default=getNumber)

    client=ForeignKey(Client, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('doc:detail', kwargs={ 'doc_id': self.id })

    def __str__(self):
        if self.number < 10:
            return self.doctype + " / " + "00" + str(self.number)
        elif self.number < 100:
            return self.doctype + " / " + "0" + str(self.number)
        else:
            return " " + self.doctype + " / " + str(self.number)



class income(models.Model):
    docum = ForeignKey(Doc, on_delete=models.CASCADE)
    product = ForeignKey(Product, on_delete=models.CASCADE)
    quantity = FloatField()
    price = FloatField()


    def count_value(self):
        ''' self.value = self.price * self.quantity '''
        return self.price * self.quantity

    value = FloatField(default=count_value)

    def __str__(self):
        return str(self.docum) + " operacja nr " + str(self.id)
'''
class expenditure(models.Model):
	number = ForeignKey(Doc, on_delete=models.CASCADE)
	product = ForeignKey(Product, on_delete=models.CASCADE)
	quantity = IntegerField()
	price = FloatField()
	value = FloatField()

'''
