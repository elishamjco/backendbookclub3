from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Genre
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
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

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('home')

def GenreView(request, gen):
    genre = get_object_or_404(Genre, name=gen)
    genre_books = Book.objects.filter(genre=genre)
    return render(request, 'genres.html', {'gen': gen, 'genre_books': genre_books})