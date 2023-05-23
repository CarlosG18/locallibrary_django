from django.urls import path
from . import views 

app_name = "catalog"
urlpatterns = [
  path("", views.index, name="index"),
  path("books/", views.books, name="books"),
  path("authors/", views.authors, name="authors"),
  path("book/<int:id>/", views.book, name="book"),
  path("author/<int:id>/", views.author, name="author"),
]