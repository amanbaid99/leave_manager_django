from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"leaveApp/main.html")


def login(request):
    return render(request,"leaveApp/login.html")
