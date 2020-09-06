from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import datetime
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.models import User


class Employee(models.Model): 
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    no_of_leaves=models.IntegerField(null=False,validators=[MinValueValidator(1),
                                       MaxValueValidator(24)],default=24)

    def __str__(self):
        return self.user.username

   

class Leave(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,default="")
    start_date=models.DateField(auto_now_add=False)
    end_date=models.DateField(auto_now_add=False)
    req_date=models.DateTimeField(default=datetime.datetime.now())
    STATUS_OPTIONS=(
        ("Approve","Approve"),
        ("Pending","Pending"),
        ("Decline","Decline"),
    )
    approved=models.CharField(max_length=10,choices=STATUS_OPTIONS,default='Pending')

    def __str__(self):
        return self.employee.user.username

    @property
    def date_diff(self):
        return (self.start_date - self.end_date).days

    
    




