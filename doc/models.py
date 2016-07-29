from __future__ import unicode_literals

from django.db import models

from django.db.models import CharField, IntegerField, BooleanField, ForeignKey, FloatField

# Create your models here.

class Clients(models.Model):
	code = CharField(max_length=50)
	name = CharField(max_length=100)
	nip = CharField(max_length=10)
	street = CharField(max_length=100)
	number = IntegerField()
	city = CharField(max_length=50)
	zip_number = CharField(max_length=5)

	def __str__(self):
		return "  " + self.code + " " + self.name + " " + self.nip + " " + self.zip_number + " " + self.city + " " + self.street + " " + str(self.number)

class ProductList(models.Model):
	itswine = BooleanField(default=True)
	name = CharField(max_length=50)
	year = CharField(max_length=4)
	color = CharField(max_length=15)
	dryness = CharField(max_length=20)

	def __str__(self):
		return self.name + " " + self.year + " " + self.color + " " + self.dryness

class DocList(models.Model):

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

	
	def getNumber(self):
		return DocList.objects.order_by('number').first().number + 1
	
	def __str__(self):
		if self.number < 10:
			return self.doctype + " / " + "00" + str(self.number)
		elif self.number < 100:
			return self.doctype + " / " + "0" + str(self.number)
		else:
			return " " + self.doctype + " / " + str(self.number)
'''

class income(models.Model):
	number = ForeignKey(DocList, on_delete=models.CASCADE)
	name = ForeignKey(ProductList, on_delete=models.CASCADE)
	quantity = IntegerField()
	price = FloatField()
	value = FloatField()

	def valueCalculation(p, q):
		return q*p

	value = valueCalculation(price, float(quantity))

class expenditure(models.Model):
	number = ForeignKey(DocList, on_delete=models.CASCADE)
	name = ForeignKey(ProductList, on_delete=models.CASCADE)
	quantity = IntegerField()
	price = FloatField()
	value = FloatField()

	def valueCalculation(p, q):
		return q*p

	value = valueCalculation(price, quantity)
'''