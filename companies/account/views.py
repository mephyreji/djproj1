from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def log(request):
    if request.method=="GET":
         return render(request,"login.html")
    elif request.method=="POST":
        print(request.POST.get("uname"))
        print(request.POST.get("password"))
        return HttpResponse("Post request reached")    
def reg(request):
    if request.method=="GET":
         return render(request,"registration.html")
    elif request.method=="POST":
        print(request.POST.get("first name"))
        print(request.POST.get("surname"))
        print(request.POST.get("email"))
        print(request.POST.get("uname"))
        print(request.POST.get("password"))
        print(request.POST.get("comfirm password"))
        return HttpResponse("Post request reached")
