from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import datetime
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.models import User


class Employee(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    EMPLOYEE='employee'
    MANAGER='manager'
    # ADMIN='admin'
    USER_TYPE=[
        (EMPLOYEE,'employee'),
        (MANAGER,'manager'),
        # (ADMIN,'admin'),
    ]
    e_type=models.CharField(max_length=10,choices=USER_TYPE,default=EMPLOYEE)
    no_of_leaves=models.IntegerField(null=False,validators=[MinValueValidator(1),
                                       MaxValueValidator(24)],default=24)

    def __str__(self):
        return self.user.username

   

class Leave(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False,blank=True)
    start_date=models.DateField(auto_now_add=False)
    end_date=models.DateField(auto_now_add=False)
    # req_date=models.DateTimeField(default=datetime.datetime.now())
    approved=models.BooleanField(default=False,null=True,blank=False)

    
    




