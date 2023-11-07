from django.urls import path
from .views import HomeView, BookDetail, AddBookView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('book/<int:pk>', BookDetail.as_view(), name="book-details"),
    path('add_book/', AddBookView.as_view(), name="add-book" )
]