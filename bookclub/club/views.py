from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Genre, Club, Reviews, Message
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

class ClubDetail(DetailView):
    model = Club
    template_name = 'club_details.html'

class AddClubView(CreateView):
    model = Club
    template_name = 'add_club.html'
    fields = '__all__'

class UpdateClubView(UpdateView):
    model = Club
    template_name = 'update_club.html'
    fields = '__all__'

class DeleteClubView(DeleteView):
    model = Club
    template_name = 'delete_club.html'
    success_url = reverse_lazy('home')

class ClubsView(ListView):
    model = Club
    template_name = 'clubs.html'

class BooksView(ListView):
    model = Book
    template_name = 'books.html'


class PostMessageView(CreateView):
    model = Message
    template_name = 'post_message.html'
    fields = '__all__'

class PostReviewView(CreateView):
    model = Reviews
    template_name = 'post_review.html'
    fields = ['book', 'text', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class UpdateMessageView(UpdateView):
    model = Message
    template_name = 'update_message.html'
    fields = '__all__'

class UpdateReviewView(UpdateView):
    model = Reviews
    template_name = 'update_reviews.html'
    fields = '__all__'

class DeleteMessageView(DeleteView):
    model = Message
    template_name = 'delete_message.html'
    success_url = reverse_lazy('clubs')

class DeleteReviewView(DeleteView):
    model = Reviews
    template_name = 'delete_review.html'
    success_url = reverse_lazy('books')

def GenreView(request, gen):
    genre = get_object_or_404(Genre, name=gen)
    genre_books = Book.objects.filter(genre=genre)
    return render(request, 'genres.html', {'gen': gen, 'genre_books': genre_books})