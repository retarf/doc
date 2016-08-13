from django.contrib import admin
from .models import Doc, Client, Product

# Register your models here.

admin.site.register(Doc)
admin.site.register(Client)
admin.site.register(Product)
