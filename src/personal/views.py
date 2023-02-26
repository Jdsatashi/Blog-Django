from operator import attrgetter
from django.shortcuts import render
from blog.models import *
from blog.views import get_blog_queries
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

BLOG_POSTS_PER_PAGE = 3

# Create your views here.
def home_screen_view(request):
    
    # context = {}
    # context['string_test'] = "this is the string to test the context."
    # context['string_2'] = "this is the second string test."
    # context = {
    #     'string_test' : "this is the string to test the context.",
    #     'string_2' : "this is the second string test."
    # }
    # list_value = []
    # list_value.append("test 01")
    # list_value.append("test 02")
    # list_value.append("test 03")
    # context['list_value'] = list_value

    context = {}


    query = ""
    if request.GET:
        query = request.GET.get('q', ' ')
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queries(query), key=attrgetter('date_updated'), reverse=True)

    #paginate    
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, 1)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(1)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)
    context['blog_posts'] = blog_posts

    return render(request, 'personal/home.html', context)
    