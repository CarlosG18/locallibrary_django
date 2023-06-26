from django.contrib import admin
from .models import Author, Book, BookUnstance, Genre, Language

class BookInstanceInline(admin.TabularInline):
    model = BookUnstance

class BookInline(admin.StackedInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'born_date', 'death_date')
    fields = [('first_name', 'last_name'), ('born_date', 'death_date')]
    inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    

@admin.register(BookUnstance)
class BookUnstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint','id')
        }),
        ('Availability',{
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


#admin.site.register(Book, BookAdmin)
#admin.site.register(BookUnstance, BookUnstanceAdmin)
#admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)

