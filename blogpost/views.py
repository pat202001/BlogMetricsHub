from django.shortcuts import render
# from urllib import request
from django.http import HttpResponse
# Create your views here.

def index(request):
 name ='index'
 return render(request,'index.html',{'name': name})


def about(request):
  name="about"
  return render(request,'about.html',{'name':name})

# def category():
#     name="category"
#     return render(request,'category.html',{'name':name})

# def contact():
#     name="contact"
#     return render(request,'contact.html',{'name':name})

# def search_result():
#     name="search-result"
#     return render(request,'search-result.html',{'name':name})

# def single_post():
#     name="single_post"
#     return render(request,'single_post.html',{'name':name})
# from django.views import generic
# from .models import blogPost

# class blogPostList(generic.ListView):
#     queryset = blogPost.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

# class PostDetail(generic.DetailView):
#     model = blogPost
#     template_name = 'blogPost_detail.html'
