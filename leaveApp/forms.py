from django import forms
from django.contrib.auth.models import User
from .models import Employee



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password','is_staff','is_superuser')
       

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields = ('no_of_leaves',)
