from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

import blogpost
from .models import Category
from blogpost.models import blogPost 

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    blog_posts = blogpost.objects.filter(categories=category)
    return render(request, 'category/category_detail.html', {'category': category, 'blog_posts': blog_posts})
