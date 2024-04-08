from django.shortcuts import render,redirect
from .models import AuthorModel,BookModel,ReviewsModel
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Avg

# Create your views here.


def home(request):
    books = BookModel.objects.annotate(averageRating=Avg('reviews__rating'))
    # The annotate function allows you to annotate (or add) extra fields
    # to each object in a QuerySet. These extra fields are computed from other 
    #fields or related data. The annotate function doesn't modify the underlying database table; 
    #it operates only in Python memory
    # You can use annotate with aggregate functions like Avg, Max, Min, Sum, Count, etc.
    
    #books = BookModel.objects.annotate(
#     num_authors=Count('authors'),
#     avg_rating=Avg('reviews__rating')
# )
    dictionary={
        'books':books
    }
    return render(request, 'Books/index.html',context=dictionary)




def bookDetail(request,book_id):
    book=BookModel.objects.get(pk=book_id)
    reviews=ReviewsModel.objects.filter(book=book)
    dictionary={
        'book':book,
        'reviews':reviews
    }
    return render(request, 'Books/details_book.html',context=dictionary)