from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils import timezone
from .models import Reader, Book, BookLoan
from .forms import ReaderForm


def main(request):
    readers = Reader.objects.all()
    error = ''

    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']

        existing_readers = Reader.objects.filter(
            Q(last_name=last_name) & Q(first_name=first_name) & Q(middle_name=middle_name))

        if existing_readers.exists():
            error = "Такой пользователь уже существует"
        else:
            reader = Reader(last_name=last_name, first_name=first_name, middle_name=middle_name)
            reader.save()

    form = ReaderForm()

    data = {
        'readers': readers,
        'form': form,
        'error': error
    }

    return render(request, 'library/readers.html', data)


def reader_detail(request, reader_id):
    # reader = get_object_or_404(Reader, pk=reader_id)
    # books = Book.objects.filter(is_available=True)
    # error = ''
    #
    # if request.method == 'POST':
    #     book_pk = request.POST.get('book_pk')
    #     try:
    #         book = Book.objects.get(pk=book_pk)
    #         if book.is_available:
    #
    #             BookLoan.objects.create(reader=reader, book=book)
    #             book.is_available = False
    #             book.save()
    #         else:
    #             error = "Книга в данный момент не доступна"
    #     except Book.DoesNotExist:
    #         error = "Книги с таким кодом нет в библиотеке"
    #
    # data = {
    #     'reader': reader,
    #     'books': books,
    #     'error': error
    # }

    reader = get_object_or_404(Reader, pk=reader_id)
    # books = Book.objects.filter(reader=reader)
    # books = BookLoan.objects.filter(reader=reader)

    data = {
        'reader': reader,
        # 'books': books
    }

    return render(request, 'library/reader_detail.html', data)


def book_list(request, reader_id):
    reader = get_object_or_404(Reader, pk=reader_id)
    books = Book.objects.filter(is_available=True)
    error = ''

    if request.method == 'POST':
        book_pk = request.POST.get('book_pk')
        try:
            book = Book.objects.get(pk=book_pk)
            if book.is_available:

                BookLoan.objects.create(reader=reader, book=book)
                book.is_available = False
                book.save()
            else:
                error = "Книга в данный момент не доступна"
        except Book.DoesNotExist:
            error = "Книги с таким кодом нет в библиотеке"

    data = {
        'reader': reader,
        'books': books,
        'error': error
    }
    return render(request, 'library/book_list.html', data)


def return_book(request, reader_id):
    reader = get_object_or_404(Reader, pk=reader_id)
    error = ''

    if request.method == 'POST':
        book_pk = request.POST.get('book_pk')
        try:
            book_loan = BookLoan.objects.get(book__pk=book_pk, reader=reader, return_date__isnull=True)
            book_loan.return_date = timezone.now()
            book_loan.save()
            book = book_loan.book
            book.is_available = True
            book.save()
        except BookLoan.DoesNotExist:
            error = "Вы не арендовали эту книгу"

    data = {
        'reader': reader,
        'error': error
    }

    return render(request, 'library/return_book.html', data)
