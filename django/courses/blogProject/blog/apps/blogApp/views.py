from django.shortcuts import render,redirect
from apps.blogApp.models import BlogModel, BlogCategory, CommentModel, ReactionModel

# Create your views here.


def index(request):
    blogs=BlogModel.objects.all().order_by('-date_posted')
    categories=BlogCategory.objects.all()
    context={
        'blogs':blogs,
        'categories':categories,
    }
    return render(request,'Blog/index.html',context)