from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book, Club, Reviews, Message
from .serializers import (
    BookSerializer, ClubSerializer, ReviewsSerializer, MessageSerializer
)

class HomeApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AddBookApiView(generics.CreateAPIView):
    serializer_class = BookSerializer

class UpdateBookApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteBookApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ClubDetailApiView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class AddClubApiView(generics.CreateAPIView):
    serializer_class = ClubSerializer

class UpdateClubApiView(generics.UpdateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class DeleteClubApiView(generics.DestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubsApiView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class BooksApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PostMessageApiView(generics.CreateAPIView):
    serializer_class = MessageSerializer

class PostReviewApiView(generics.CreateAPIView):
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UpdateMessageApiView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UpdateReviewApiView(generics.UpdateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class DeleteMessageApiView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class DeleteReviewApiView(generics.DestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer