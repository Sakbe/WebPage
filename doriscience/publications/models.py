from django.db import models
from datetime import datetime

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=500, default="Publication Title")
    journal = models.CharField(max_length=300, default="Journal, vol. X, pp. Y", null=True)
    authors = models.CharField(max_length=400, default="D. Corona")
    date = models.DateField(default=datetime.now)
    pubfile = models.FileField(upload_to='publications/', null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        ordering = ['order']
        
    def date_pretty(self):
        return self.date.strftime('%Y')

    def __str__(self):
        return self.date.strftime('%Y')+" - "+self.title

class Quote(models.Model):
    text = models.CharField(max_length=350, default="Te amo Dori")
    author = models.CharField(max_length=350, default="Anonymous")
    is_active = models.BooleanField(default=True, blank=False, null=False)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        ordering = ['order']
    
    def __str__(self):
        return self.author+" - "+self.text