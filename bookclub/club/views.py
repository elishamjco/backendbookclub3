from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
# Create your views here.

class HomeView(ListView):
    model = Book
    template_name = 'home.html'

class BookDetail(DetailView):
    model = Book
    template_name = 'book_details.html'