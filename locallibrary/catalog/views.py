from django.shortcuts import render
from .models import Book, Author, BookUnstance, Genre, Language
from django.views import generic

def index(request):
  num_books = Book.objects.all().count()
  num_intances = BookUnstance.objects.all().count()
  num_intances_available = BookUnstance.objects.filter(status__exact='a').count()
  num_authors = Author.objects.all().count()

  num_visitas = request.session.get('num_visitas', 0)
  request.session['num_visitas'] = num_visitas+1

  context = {
    'num_books': num_books,
    "num_instances": num_intances,
    "num_instances_available": num_intances_available,
    "num_authors": num_authors,
    "num_visitas": num_visitas,
  }
  return render(request, "catalog/index.html", context=context)
  
class BookListView(generic.ListView):
  model = Book
  paginate_by = 3
  context_object_name = "livros"
  queryset = Book.objects.all()
  template_name = "catalog/books.html"
  
class BookDetailView(generic.DetailView):
  model = Book

#def books(request):
#  books = Book.objects.all()  
#  return render(request, "catalog/books.html", {
#    "livros": books,
#  })

class AuthorListView(generic.ListView):
  model = Author
  context_object_name = "authors"
  template_name = "catalog/authors.html"

class AuthorDetailView(generic.DetailView):
  model = Author  
  
#def authors(request):
#  autores = Author.objects.all()
#  return render(request, "catalog/authors.html", {
#    "authors": autores,
#  })
  
#def book_detail(request, id):
#  return HttpResponse(f'book id = {id}')

#def author(request, id):
#  return HttpResponse(f'authors id =  {id}')