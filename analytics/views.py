from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
# Create your views here.

def analytics(request):
 name ='analytics'
 return render(request,'analytics.html',{'analytics': name})