from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from blog.models import BlogPost
from blog.forms import * 
from account.models import Account

def create_blog_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authentication')

    forms = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if forms.is_valid():
        obj = forms.save(commit=False)
        author = Account.objects.filter(email = user.email).first()
        obj.author = author
        obj.save()
        forms = CreateBlogPostForm()

    context['form'] = forms

    return render(request,'blog/create_blog.html', context)

def view_blog_detail(request, slug):
    context = {}
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post
    return render(request, 'blog/detail_blog.html', context)

def edit_blog_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authentication')

    blog_post = get_object_or_404(BlogPost, slug=slug)    
    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = 'Blog has been updated successfully.'
            blog_post = obj

    form = UpdateBlogPostForm(
        initial= {
            "title" : blog_post.title,
            "body" : blog_post.body,
            "image" : blog_post.image
        }
    )

    context['form'] = form
    return render(request, 'blog/update.html', context)

def get_blog_queries(query = None):
    queries = []
    query = query.split(" ")
    for q in query:
        posts = BlogPost.objects.filter(
            Q(title__icontains=q) |
            Q(body__icontains=q)
        ).distinct()

        for post in posts:
            queries.append(post)

    return list(set(queries))