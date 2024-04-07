from django.shortcuts import render,redirect
from .models import AuthorModel,BookModel,ReviewsModel
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def home(request):
    books=BookModel.objects.all()
    dictionary={
        'books':books
    }
    return render(request, 'Books/index.html',context=dictionary)