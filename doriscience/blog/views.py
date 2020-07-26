from django.shortcuts import render, get_object_or_404
from .models import Entry

# Create your views here.
def allentries(request):
    entries = Entry.objects.order_by('-date')
    return render(request, 'blog/allentries.html', {'entries':entries, 'nav':'blog'})

def entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/entry.html', {'entry':entry, 'nav':'blog'})