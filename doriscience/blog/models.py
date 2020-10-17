from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.
class Entry(models.Model):
    is_active = models.BooleanField(default=True, blank=False, null=False)
    title = models.CharField(max_length=140)
    date = models.DateTimeField(default=datetime.now)
    tags = models.CharField(max_length=200)
    body = models.TextField()
    class Meta(object):
        ordering = ['-date']

    def cover(self):
        return self.images.filter(is_cover=True).first()

    def gallery_images(self):
        return self.images.filter(in_gallery=True).all()

    def date_pretty(self):
        return self.date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title

class File(models.Model):
    name = models.CharField(max_length=80, default="File name")
    description = models.CharField(max_length=140, default="File description", blank=True)
    order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True
        ordering = ['order']
    def __str__(self):
        return self.name

def validate_image(image):
    max_width = 2048
    max_height = 2048
    height = image.height 
    width = image.width
    error_message = "Image height or width is larger than allowed: "+str(max_width)+"x"+str(max_height)
    if width > max_width or height > max_height:
        raise ValidationError(error_message)

class Image(File):
    entry = models.ForeignKey(Entry, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/images/', validators=[validate_image])
    in_gallery = models.BooleanField(default=False)
    is_cover = models.BooleanField(default=False)

class GalleryEmbed(File):
    entry = models.ForeignKey(Entry, related_name='gallery_embeds', on_delete=models.CASCADE)
    body = models.TextField(default="Embed <iframe>")
