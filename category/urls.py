from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='list'),
    path('<int:category_id>/', views.category_detail, name='detail'),
]
