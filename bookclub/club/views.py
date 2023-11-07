from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Book
# Create your views here.

class HomeView(ListView):
    model = Book
    template_name = 'home.html'

class BookDetail(DetailView):
    model = Book
    template_name = 'book_details.html'

class AddBookView(CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = '__all__'

class UpdateBookView(UpdateView):
    model = Book
    template_name = 'update_book.html'
    fields = '__all__'