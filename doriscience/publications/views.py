from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

from .models import Publication, Quote

# Create your views here.
def all(request):
    pubs = Publication.objects.order_by('order')
    quote = Quote.objects.first
    return render(request, 'publications/list.html', 
    {
        'pubs': pubs,
        'quote': quote,
    })
