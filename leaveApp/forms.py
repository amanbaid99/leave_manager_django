from django import forms
from django.contrib.auth.models import User
from .models import Employee,Leave


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password','is_staff','is_superuser')
       

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields = ('no_of_leaves',)

class DateInput(forms.DateInput):
    input_type = 'date'

class leaveForm(forms.ModelForm):

    class Meta():
        model = Leave
        fields = ('title','employee','start_date','end_date','description')
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
            'employee':forms.HiddenInput(),
        }

 
