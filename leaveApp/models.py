from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import datetime

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100,null=False)
    e_id=models.CharField(max_length=25, null=False)
    password=models.CharField(max_length=100,null=False)
    EMPLOYEE='em'
    MANAGER='mn'
    USER_TYPE=[
        (EMPLOYEE,'employee'),
        (MANAGER,'manager'),
    ]
    e_type=models.CharField(max_length=2,choices=USER_TYPE,default=EMPLOYEE)
    no_of_leaves=models.IntegerField(null=False,validators=[MinValueValidator(1),
                                       MaxValueValidator(24)],default=24)


    def __str__(self):
        return self.e_id
        

class Leave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=True)
    start_date=models.DateField(auto_now_add=False)
    end_date=models.DateField(auto_now_add=False)
    req_date=models.DateTimeField(default=datetime.datetime.now())
    approved=models.BooleanField(default=False,null=True,blank=False)

    
    




