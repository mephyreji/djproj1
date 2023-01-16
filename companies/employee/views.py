from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>hello all,welcome to django </h1>")
def home(req):
    name="aswathy"
    last=["vismaya","mephy","dil"]
    exp=0
    return render(req,"home.html",{"data":name,"list":last,"cndn":exp})
