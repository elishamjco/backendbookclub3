from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Book(models.Model):
    book = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.book


    def get_absolute_url(self):
        return reverse('home')

class Reviews(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    time = models.DateTimeField()

    def __str__(self):
        return self.book + self.user
    def get_absolute_url(self):
        return reverse('home')

class Club(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    description= models.TextField(blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.user
    def get_absolute_url(self):
        return reverse('home')