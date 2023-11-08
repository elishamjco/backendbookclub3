from django.contrib import admin
from .models import Book, Genre, Message, Club, Reviews

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Message)
admin.site.register(Club)
admin.site.register(Reviews)
