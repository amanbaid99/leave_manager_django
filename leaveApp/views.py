from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .models import *
from django.views.generic import TemplateView
from .forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    user=request.user
    u=User.objects.get(username=user)
    
    leave_pending=Leave.objects.filter(approved="Pending")
    leave_approved=Leave.objects.filter(approved="Approved")
    leave_declined=Leave.objects.filter(approved="Declined")
    
    nofleaves=None
    if user.is_superuser:
        pass
    else: 
        e=Employee.objects.get(user=user.id)
        nofleaves=u.employee.no_of_leaves
    context={'nofleaves':nofleaves,'leave_pending':leave_pending,'leave_approved':leave_approved,
                                                                'leave_declined':leave_declined,}
    return render(request,"leaveApp/home.html",context)


@login_required
def register(request):
  
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

      
        if user_form.is_valid() and profile_form.is_valid():  
            user = user_form.save() 
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
  
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'leaveApp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,})





class LogOutView(TemplateView):
    template_name = "leaveApp/home.html"

class LogInView(TemplateView):
    template_name="leaveApp/home.html"

