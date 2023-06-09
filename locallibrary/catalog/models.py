from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import date
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Entre com o genero do livro (ex.: ficção)')

    def __str__(self):
        return self.name

class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='entre com uma descrição do livro')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='selecione o genero do livro')
    language = models.ForeignKey('Language',on_delete=models.SET_NULL, null=True)

    # author é ForeignKey por que um livro so tera um autor, porem um autor pode ter varios livros de sua autoria
    # já genre e manytomanyfield porque um livro pode possuir varios generos

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:book_detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

        display_genre.short_description = 'Genre'


class BookUnstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='id unico para um livro particular')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "set book as returned"),)

    def __str__(self):
        return f'{self.id} ({self.book.title})'

    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born_date = models.DateField(null=True, blank=True)
    death_date = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name