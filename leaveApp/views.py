from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .models import *
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return render(request,"leaveApp/main.html")


class LogOutView(TemplateView):
    template_name = "leaveApp/main.html"

