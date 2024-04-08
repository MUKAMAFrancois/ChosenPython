from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,SignUpForm
from django.contrib import messages

# Create your views here.



def signup_view(request):
    
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['confirm_password']
            if password==confirm_password:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect('signup')
                else:
                    user=User.objects.create_user(first_name=first_name,
                                                  last_name=last_name,
                                                  email=email,
                                                  password=password, 
                                                  username=email)
                    user.save()
                    messages.success(request,'Account created successfully')
                    return redirect('login')
            else:
                messages.error(request,'Passwords do not match')
                return redirect('signup')
    else:
        form=SignUpForm()
    return render(request,'Users/auth/register.html',{'form':form})



def login_view(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request, username=User.objects.get(email=email),password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Login successful')
                return redirect('home')
            else:
                messages.error(request,'Invalid credentials')
                return redirect('login')
    else:
        form=LoginForm()
    return render(request,'Users/auth/login.html',{'form':form})