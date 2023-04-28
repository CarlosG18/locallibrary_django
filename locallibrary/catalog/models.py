from turtle import st
from django.db import models
from django.urls import reverse

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
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    name = models.CharField(max_length=200)
