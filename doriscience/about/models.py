from django.db import models
from datetime import datetime

# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=100, default="Experience Title")
    place = models.CharField(max_length=120)
    body = models.TextField()
    is_current = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)

    def start_date_pretty(self):
        return self.start_date.strftime('%b/%y')

    def end_date_pretty(self):
        return self.end_date.strftime('%b/%y')

    def __str__(self):
        return self.title + "@" + self.place

    class Meta:
        abstract = True

class WorkExperience(Experience):
    techs = models.TextField()

class Education(Experience):
    thesis = models.TextField()

    def start_date_pretty(self):
        return self.start_date.strftime('%Y')

    def end_date_pretty(self):
        return self.end_date.strftime('%Y')

class Award(models.Model):
    title = models.CharField(max_length=100, default="Award Title")
    organization = models.CharField(max_length=120)
    date = models.DateField(default=datetime.now)
    url = models.CharField(max_length=200, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    class Meta(object):
        ordering = ['order']
        
    def date_pretty(self):
        return self.date.strftime('%Y')
    
    def __str__(self):
        return self.title + " by " + self.organization

class Skill(models.Model):
    name = models.CharField(max_length=280)
    icon = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    class Meta(object):
        ordering = ['order']
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=60)
    proficiency = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        ordering = ['order']
    def __str__(self):
        return self.name

class Hobby(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to='images/hobbies/')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=False, null=False)
    class Meta(object):
        ordering = ['order']
    def __str__(self):
        return self.name