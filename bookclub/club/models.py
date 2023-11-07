from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    book = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.book
class Review(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()