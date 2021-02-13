from django.contrib import admin

#1. Importar o Model
from .models import Item

# Register your models here.
admin.site.register(Item)
