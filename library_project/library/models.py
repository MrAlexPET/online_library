from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} {self.author}"

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        db_table = 'book'


class Reader(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'
        db_table = 'reader'


class BookLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} {self.reader} {self.loan_date} {self.return_date}"

    class Meta:
        db_table = 'book_loan'
