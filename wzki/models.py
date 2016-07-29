from __future__ import unicode_literals

from django.db import models


class DocList(models.Model):

    WZ = 'WZ'
    PZ = 'PZ'
    RW = 'RW'
    PW = 'PW'

    DOC_TYPE_CHOICES = (
        (WZ, 'WZ'),
        (PZ, 'PZ'),
        (RW, 'RW'),
        (PW, 'PW'),
    )
    doc_type = models.CharField(
        max_length=2,
        choices=DOC_TYPE_CHOICES,
        default=WZ,
    )
    numeracja = models.IntegerField()

    def nadaj_numeracje(self):
        self.numeracja=DocList.objects.order_by('numeracja').first().numeracja + 1

    def __str__(self):
        return str(self.numeracja) + "/" + self.doc_type

class WineList(models.Model):

    wine_name = models.CharField(max_length=50)
    wine_year = models.CharField(max_length=4)

    Czerwone = 'Czerwone'
    Biale = 'Biale'
    Rozowe = 'Rozowe'

    WINE_COLOR_CHOICES = (
        (Czerwone, 'Czerwone'),
        (Biale, 'Biale'),
        (Rozowe, 'Rozowe'),
    )
    wine_color = models.CharField(
        max_length=8,
        choices=WINE_COLOR_CHOICES,
        default=Czerwone,
    )

    Wytrawne = 'Wytrawne'
    Polwytrawne = 'Polwytrawne'
    Slodkie = 'Slodkie'
    Polslodkie = 'Polslodkie'

    WINE_TASTE_CHOICES = (
        (Wytrawne, 'Wytrawne'),
        (Polwytrawne, 'Polwytrawne'),
        (Slodkie, 'Slodkie'),
        (Polslodkie, 'Polslodkie'),
    )
    wine_taste = models.CharField(
        max_length=8,
        choices=WINE_TASTE_CHOICES,
        default=Wytrawne,
    )