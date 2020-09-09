from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .models import *
from django.views.generic import TemplateView
from .forms import UserForm,UserProfileInfoForm,leaveForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect


def home(request):

    #general data
    user=request.user
    emp=None
    if user.is_superuser:
        pass
    else:
        emp=Employee.objects.get(user=user)

    #data for manager/adminpage
    leave_pending=Leave.objects.filter(approved="Pending")
    leave_approved=Leave.objects.filter(approved="Approved")
    leave_declined=Leave.objects.filter(approved="Declined")
    
    #data for employee
    leave_populate= Leave.objects.filter(employee=emp)
    print(leave_populate)
    context={'leave_pending':leave_pending,'leave_approved':leave_approved,
            'leave_declined':leave_declined,'leave_populate':leave_populate}
    return render(request,"leaveApp/home.html",context)


def approve(request,pk):
    leave=Leave.objects.get(id=pk)
    leave.approved="Approved"
    leave.approved_by=request.user.username
    leave.save()
    emp=leave.employee
    emp.user=leave.employee.user
    emp.no_of_leaves=(emp.no_of_leaves - leave.total_days)
    emp.save()
    return HttpResponsePermanentRedirect('/')

def decline(request,pk):
    leave=Leave.objects.get(id=pk)
    leave.approved="Declined"
    leave.approved_by=request.user.username
    leave.save()
    return HttpResponsePermanentRedirect('/')
    
    
@login_required
def applyforleave(request):
    emp=Employee.objects.get(user=request.user)
    nod=emp.no_of_leaves
    submitted= False
    exceeded=False

    if request.method == 'POST':
        leave_form = leaveForm(data=request.POST)
        if leave_form.is_valid():
            start_date=leave_form.cleaned_data['start_date']
            end_date=leave_form.cleaned_data['end_date']
            total_days=(end_date-start_date).days
            
            if total_days < nod:
                leave = leave_form.save()
                leave.employee=emp
                leave.total_days=total_days
                leave.save()
                submitted = True

            else:
                exceeded= True
        else:
            print(leave_form.errors)
    else: 
        leave_form = leaveForm()
    
    return render(request,'leaveApp/leave.html',
                          {'leave_form':leave_form,
                          'submitted':submitted,'emp':emp,'exceeded':exceeded})

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
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'leaveApp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,})


class LogOutView(TemplateView):
    template_name = "leaveApp/home.html"

class LogInView(TemplateView):
    template_name="leaveApp/home.html"






