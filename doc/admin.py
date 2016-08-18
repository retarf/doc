from django.contrib import admin
from .models import Doc, Client, Product, income

# Register your models here.

admin.site.register(Doc)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(income)