from django.contrib import admin
from.models import Author, Book, Reader, BookLoan


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass


@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    pass
