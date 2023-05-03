from django.contrib import admin
from .models import Author, Book, BookUnstance, Genre, Language

admin.site.register(Book)
admin.site.register(BookUnstance)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)

