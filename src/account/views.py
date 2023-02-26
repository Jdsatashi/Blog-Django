from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import *
from blog.models import *

def registration_view(request):
    context = {}
    if request.POST:
    #if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email= email, password=password)
            login(request, account)
            return redirect('home')
        else:
            context['regist_form'] = form
    else:
        form = RegistrationForm()
        context['regist_form'] = form
    return render(request, 'account/register.html', context)        

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AuthenticateForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticateForm()
    context['login_form'] = form
    return render(request, 'account/login.html', context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST('email'),
                "username": request.POST('username'),
            }
            form.save()
            return redirect("home")
    else:
        form = AccountUpdateForm(
            initial= {
                "email": request.user.email,
                "username": request.user.username
            }
        )    
    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts

    return render(request, 'account/account.html', context)

def must_authentication_view(request):
    return render(request, 'account/must_authentication.html', {})    

