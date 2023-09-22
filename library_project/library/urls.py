from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='readers'),
    path('readers/<int:reader_id>/', views.reader_detail, name='reader_detail'),
    path('readers/<int:reader_id>/books/', views.book_list, name='book_list'),
    path('readers/<int:reader_id>/return/', views.return_book, name='return_book'),
]
