
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('book/<int:book_id>',views.bookDetail,name='bookDetail')
    

]