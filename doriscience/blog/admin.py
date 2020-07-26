from django.contrib import admin

# Register your models here.
from .models import Entry
admin.site.registrer(Entry)