from django.db import models
from datetime import datetime

# Create your models here.
class Entry(models.Model):
    is_active = models.BooleanField(default=True, blank=False, null=False)
    title = models.CharField(max_length=140)
    cover_image = models.ImageField(upload_to='blog/images', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)
    tags = models.CharField(max_length=200)
    body = models.TextField()    

    class Meta(object):
        ordering = ['date']

    def date_pretty(self):
        return self.date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title

    