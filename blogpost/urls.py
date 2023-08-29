from django.urls import path
from .import views 

urlpatterns=[
    path('',views.index,name='index'),
    # path('about',views.about,name='about'),
    # path('categry',views.category,name='category'),
    # path('contact',views.contact,name='contact'),
    # path('search_result',views.search_result,name='search_result'),
    # path('single_post',views.single_post,name='single_post'),
    # path('', views.blogPostList.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]