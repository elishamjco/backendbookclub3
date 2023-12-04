from django.urls import path
from .views import (
    HomeApiView, BookDetailApiView, AddBookApiView, UpdateBookApiView, DeleteBookApiView,
    ClubDetailApiView, AddClubApiView, UpdateClubApiView, DeleteClubApiView, ClubsApiView,
    BooksApiView, PostMessageApiView, PostReviewApiView, UpdateMessageApiView,
    UpdateReviewApiView, DeleteMessageApiView, DeleteReviewApiView
)

urlpatterns = [
    path('api/home/', HomeApiView.as_view(), name='home-api'),
    path('api/books/<int:pk>/', BookDetailApiView.as_view(), name='book-detail-api'),
    path('api/add_book/', AddBookApiView.as_view(), name='add-book-api'),
    path('api/update_book/<int:pk>/', UpdateBookApiView.as_view(), name='update-book-api'),
    path('api/delete_book/<int:pk>/', DeleteBookApiView.as_view(), name='delete-book-api'),

    path('api/club_detail/<int:pk>/', ClubDetailApiView.as_view(), name='club-detail-api'),
    path('api/add_club/', AddClubApiView.as_view(), name='add-club-api'),
    path('api/update_club/<int:pk>/', UpdateClubApiView.as_view(), name='update-club-api'),
    path('api/delete_club/<int:pk>/', DeleteClubApiView.as_view(), name='delete-club-api'),
    path('api/clubs/', ClubsApiView.as_view(), name='clubs-api'),

    path('api/books/', BooksApiView.as_view(), name='books-api'),

    path('api/post_message/', PostMessageApiView.as_view(), name='post-message-api'),

    path('api/post_review/', PostReviewApiView.as_view(), name='post-review-api'),

    path('api/update_message/<int:pk>/', UpdateMessageApiView.as_view(), name='update-message-api'),

    path('api/update_review/<int:pk>/', UpdateReviewApiView.as_view(), name='update-review-api'),

    path('api/delete_message/<int:pk>/', DeleteMessageApiView.as_view(), name='delete-message-api'),

    path('api/delete_review/<int:pk>/', DeleteReviewApiView.as_view(), name='delete-review-api'),

]