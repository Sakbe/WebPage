from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
from .models import Publication, Quote

@admin.register(Publication)
class PublicationAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(Quote)
class QuoteAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass