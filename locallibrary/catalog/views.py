from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookUnstance, Genre, Language

def index(request):
  context = {
    
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