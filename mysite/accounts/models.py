from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import UserManager
from django.core.mail import send_mail

class Student(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=40,null=True,blank=True)
    last_name = models.CharField(max_length=40,null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    phoneno = models.IntegerField(null=True,blank=True)
    dob = models.DateTimeField(blank=True,null=True)
    profile_image = models.FileField(upload_to='pics/',null=True,blank=True)
    college_name = models.CharField(max_length=50,default='Nalanda Institute Of Technology')
    branch = models.CharField(max_length=20,null=True,blank=True)
    regdno = models.IntegerField(null=True,blank=True)
    approved = models.BooleanField(default=False)
    date_of_join = models.DateTimeField(auto_now_add=True)
    date_of_approved = models.DateTimeField(null=True,blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        
        return self.first_name +' '+ self.last_name
        #return "%s %s" %(self.first_name,self.last_name)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def approve(self):
        self.approved = True
        self.date_of_approved = timezone.now()
        send_mail(' Approved ','Dear , You are approved to learn with TheLearner','thelearnercse123@gmail.com',[self.email],fail_silently=False,)

