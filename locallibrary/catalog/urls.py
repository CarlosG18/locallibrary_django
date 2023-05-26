from django.urls import path
from . import views 

app_name = "catalog"
urlpatterns = [
  path("", views.index, name="index"),
  path("books/", views.BookListView.as_view(), name="books"),
  path("authors/", views.AuthorListView.as_view(), name="authors"),
  path("book/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
  path("author/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
]