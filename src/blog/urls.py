from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('create', create_blog_view, name="create"),
    path('<slug>/', view_blog_detail, name="detail"),
    path('<slug>/edit', edit_blog_view, name="edit")
]