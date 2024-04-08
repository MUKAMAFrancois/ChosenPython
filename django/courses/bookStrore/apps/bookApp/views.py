from django.shortcuts import render,redirect
from .models import AuthorModel,BookModel,ReviewsModel
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .forms import PostReview,PostRating

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



def bookDetail(request, book_id):
    book = BookModel.objects.get(pk=book_id)
    reviews = ReviewsModel.objects.filter(book=book).order_by('-createdAt')
    average_rating = reviews.aggregate(Avg('rating')).get('rating__avg', 0.0)
    rating_form = PostRating()  # Initialize rating_form with default value
    review_form = PostReview()

    if request.method == 'POST':
        if 'rating_form' in request.POST:
            rating_form = PostRating(request.POST)
            if rating_form.is_valid():
                rating = rating_form.cleaned_data['rating']
                newRating = ReviewsModel(rating=rating, book=book)
                newRating.save()
                messages.success(request, 'Thank you for your Rating!')
                return redirect('bookDetail', book_id=book_id)
        else:
            review_form = PostReview(request.POST)
            if review_form.is_valid():
                review = review_form.cleaned_data['review']
                user = request.user
                newReview = ReviewsModel(book=book, reviewer=user, reviewContent=review)
                newReview.save()
                messages.success(request, 'Your Review have been submitted')
                return redirect('bookDetail', book_id=book_id)

    dictionary = {
        'book': book,
        'review_form': review_form,
        'reviews': reviews,
        'rating_form': rating_form,
        'average_rating': average_rating,
    }
    return render(request, 'Books/details_book.html', context=dictionary)



