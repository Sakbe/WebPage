from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
# Register your models here.
from .models import Entry, Image, GalleryEmbed

class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image
    extra = 1

class GalleryEmbedInline(SortableInlineAdminMixin, admin.StackedInline):
    model = GalleryEmbed
    extra = 1

class EntryAdmin(admin.ModelAdmin):
    inlines = [ ImageInline, GalleryEmbedInline ]
    ordering = ['-date']

admin.site.register(Entry, EntryAdmin)