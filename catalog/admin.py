from django.contrib import admin
from .models import Author, Genre, Language, Book, BookInstance


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
  pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
  pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_filter = ('status', 'due_back')
