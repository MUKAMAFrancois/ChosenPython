from django.shortcuts import render,redirect
from apps.blogApp.models import BlogModel, BlogCategory, CommentModel, ReactionModel
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    blogs=BlogModel.objects.all().order_by('-date_posted')
    categories=BlogCategory.objects.all()
    context={
        'blogs':blogs,
        'categories':categories,
    }
    return render(request,'Blog/index.html',context)



def detailed_page(request,blog_id):
    blog=BlogModel.objects.get(id=blog_id)
    comments=CommentModel.objects.filter(blog=blog)
    likes=ReactionModel.objects.filter(blog=blog,reaction=1).count()
    dislikes=ReactionModel.objects.filter(blog=blog,reaction=-1).count()
    
    context={
        'blog':blog,
        'comments':comments,
        'likes':likes,
        'dislikes':dislikes,
    }
    return render(request,'Blog/detailed_page.html',context)

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form=BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            content=form.cleaned_data['content']
            categories=form.cleaned_data['category']
            image=form.cleaned_data['image']
            blog=BlogModel(title=title,
                           content=content,
                           image=image,
                           author=request.user.person)
            blog.category.set(categories) # set many to many relationship
            blog.save()
            return redirect('create_blog')
    else:
        form=BlogPostForm()
    return render(request,'Blog/add_blog.html',{'form':form})