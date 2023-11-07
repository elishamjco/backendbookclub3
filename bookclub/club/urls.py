from django.urls import path
from .views import HomeView, BookDetail, AddBookView, UpdateBookView, DeleteBookView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('book/<int:pk>', BookDetail.as_view(), name="book-details"),
    path('add_book/', AddBookView.as_view(), name="add-book" ),
    path('book/edit/<int:pk>', UpdateBookView.as_view(), name="edit-book" ),
    path('book/<int:pk>/remove', DeleteBookView.as_view(), name="delete-book" ),
]