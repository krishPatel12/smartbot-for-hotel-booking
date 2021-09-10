from django.shortcuts import render

def home(request,*args):
    return render(request,"user/home.html")

def hotel1(request,*args):
    return render(request,"user/hotel1.html")
