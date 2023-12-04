from django.urls import path
from .views import HomeView, BookDetail, AddBookView, UpdateBookView, DeleteBookView, ClubDetail, AddClubView, UpdateClubView, DeleteClubView, ClubsView, BooksView, PostMessageView, PostReviewView, UpdateMessageView, UpdateReviewView, DeleteMessageView, DeleteReviewView, GenreView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('books/', BooksView.as_view(), name="books"),
    path('clubs/', ClubsView.as_view(), name="clubs"),
    path('club/<int:pk>', ClubDetail.as_view(), name="club-details"),
    path('add_club/', AddClubView.as_view(), name="add-club"),
    path('club/edit/<int:pk>', UpdateClubView.as_view(), name="edit-club"),
    path('club/<int:pk>/remove', DeleteClubView.as_view(), name="delete-club"),
    path('book/<int:pk>', BookDetail.as_view(), name="book-details"),
    path('add_book/', AddBookView.as_view(), name="add-book" ),
    path('book/edit/<int:pk>', UpdateBookView.as_view(), name="edit-book" ),
    path('book/<int:pk>/remove', DeleteBookView.as_view(), name="delete-book" ),
    path('post_message/', PostMessageView.as_view(), name="post-message"),
    path('message/edit/<int:pk>', UpdateMessageView.as_view(), name="edit-message"),
    path('message/<int:pk>/remove', DeleteMessageView.as_view(), name="delete-message"),
    path('post_review/', PostReviewView.as_view(), name="post-review"),
    path('review/edit/<int:pk>', UpdateReviewView.as_view(), name="edit-review"),
    path('review/<int:pk>/remove', DeleteReviewView.as_view(), name="delete-review"),
    path('genre/<str:gen>/', GenreView, name="genre" )
]