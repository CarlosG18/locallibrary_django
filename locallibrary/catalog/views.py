from re import template
from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookUnstance, Genre, Language
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django import forms
from .forms import FormDueBack
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
  # help(forms.fields)
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

class ListBookInstance(LoginRequiredMixin, generic.ListView):
  model = BookUnstance
  template_name = "catalog/list_books_instances.html"
  paginate_by = 10

  def get_queryset(self):
    return(
      BookUnstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
    )

class ListBookNoReturn(PermissionRequiredMixin,LoginRequiredMixin,generic.ListView):
  permission_required = "can_mark_returned"
  model = BookUnstance
  template_name = "catalog/booksnoreturn.html"
  paginate_by = 10

  def get_queryset(self):
      return (
        BookUnstance.objects.filter(status__exact='r')
      )

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
  book_instance = get_object_or_404(BookUnstance, pk=pk)

  if request.method == "POST":
    form = FormDueBack(request.POST)
    if form.is_valid():
      book_instance.due_back = form.cleaned_data['new_date']
      book_instance.save()
      return HttpResponseRedirect(reverse('catalog:home'))
  else:
    suposta_new_date = datetime.date.today() + datetime.timedelta(weeks=3)
    form = FormDueBack(initial={'new_date': suposta_new_date})
  return render(request, 'catalog/form_renew_book.html', {
    'form': form,
    'book_instace': book_instance,
  })

  