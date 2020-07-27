from django.http import HttpResponse
from django.shortcuts import render
from math import factorial

def index(request):
    return HttpResponse("<h1>welcome to views of app </h1>")

def home(request):
    return render(request,"Myapp/home.html",{'name':"mallika"})

def fact(request,n):
    n=int(n)
    return HttpResponse("<h2> factorial is {} </h2>".format(factorial(n)))
