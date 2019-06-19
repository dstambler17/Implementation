import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length = 500)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    date_posted = models.DateField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catagories = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=100, db_index=True, default="hi")

    def __str__(self):
        return self.title

    def get_month(self):
        thedate = self.date_posted
        return thedate.strftime("%B")

    def get_year(self):
        thedate = self.date_posted
        return thedate.strftime("%Y")

class Podcast(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length = 500)
    date_posted = models.DateField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catagories = models.ManyToManyField(Category)
    audio_file = models.FileField(upload_to='audio/')
    slug = models.SlugField(max_length=100, db_index=True, default="Please enter here")

    def __str__(self):
        return self.title
