
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('book/<int:book_id>',views.bookDetail,name='bookDetail'),
    path('author/<int:author_id>/books', views.books_by_same_author, name='books_by_same_author'),
    

]