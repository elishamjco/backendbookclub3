from django.urls import path
from .views import HomeView, BookDetail, AddBookView, UpdateBookView, DeleteBookView, ClubDetail, AddClubView, UpdateClubView, DeleteClubView, GenreView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('club/<int:pk>', ClubDetail.as_view(), name="club-details"),
    path('add_club/', AddClubView.as_view(), name="add-club"),
    path('club/edit/<int:pk>', UpdateClubView.as_view(), name="edit-club"),
    path('club/<int:pk>/remove', DeleteClubView.as_view(), name="delete-club"),
    path('book/<int:pk>', BookDetail.as_view(), name="book-details"),
    path('add_book/', AddBookView.as_view(), name="add-book" ),
    path('book/edit/<int:pk>', UpdateBookView.as_view(), name="edit-book" ),
    path('book/<int:pk>/remove', DeleteBookView.as_view(), name="delete-book" ),
    path('genre/<str:gen>/', GenreView, name="genre" )
]