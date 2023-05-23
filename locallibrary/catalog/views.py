from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookUnstance, Genre, Language

def index(request):
  num_books = Book.objects.all().count()
  num_intances = BookUnstance.objects.all().count()
  num_intances_available = BookUnstance.objects.filter(status__exact='a').count()
  num_authors = Author.objects.all().count()
  context = {
    'num_books': num_books,
    "num_intances": num_intances,
    "num_intances_available": num_intances_available,
    "num_authors": num_authors,
  }
  return render(request, "catalog/index.html", context=context)
  
def books(request):
  return HttpResponse("books")
  
def authors(request):
  return HttpResponse("authors")
  
def book(request, id):
  return HttpResponse(f'book id = {id}')

def author(request, id):
  return HttpResponse(f'authors id =  {id}')