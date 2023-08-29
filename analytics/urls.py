from django.urls import path
from .views import views

urlspatterns=[
path(' ',views.analytics,name='analytics'),
]