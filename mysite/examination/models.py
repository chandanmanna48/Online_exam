from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Aptitude(models.Model):
    qno = models.IntegerField(null=True,blank=True)
    question = models.TextField(null=True,blank=True)
    option1 = models.CharField(max_length=100,null=True,blank=True)
    option2 = models.CharField(max_length=100,null=True,blank=True)
    option3 = models.CharField(max_length=100,null=True,blank=True)
    option4 = models.CharField(max_length=100,null=True,blank=True)
    answer = models.CharField(max_length=100,null=True,blank=True)
    user_select = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.qno) + " . " + self.question

class Reasogning(models.Model):
    qno = models.IntegerField(null=True,blank=True)
    question = models.TextField(null=True,blank=True)
    option1 = models.CharField(max_length=100,null=True,blank=True)
    option2 = models.CharField(max_length=100,null=True,blank=True)
    option3 = models.CharField(max_length=100,null=True,blank=True)
    option4 = models.CharField(max_length=100,null=True,blank=True)
    answer = models.CharField(max_length=100,null=True,blank=True)
    user_select = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.qno) + " . " + self.question

class GeneralKnowledge(models.Model):
    qno = models.IntegerField(null=True,blank=True)
    question = models.TextField(null=True,blank=True)
    option1 = models.CharField(max_length=100,null=True,blank=True)
    option2 = models.CharField(max_length=100,null=True,blank=True)
    option3 = models.CharField(max_length=100,null=True,blank=True)
    option4 = models.CharField(max_length=100,null=True,blank=True)
    answer = models.CharField(max_length=100,null=True,blank=True)
    user_select = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.qno) + " . " + self.question

class Add_Aptitude_sample(models.Model):
    Name = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.FileField(null=True,blank=True,upload_to='pics/')
    file = models.FileField(null=True,blank=True,upload_to='documents/')
    full_name = str(User.first_name) + str(User.last_name)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,default='Admin',null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name

class Add_Reasogning_sample(models.Model):
    Name = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.FileField(null=True,blank=True,upload_to='pics/')
    file = models.FileField(null=True,blank=True,upload_to='documents/')
    full_name = str(User.first_name) + str(User.last_name)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,default='Admin',null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name

class Add_GeneralKnowledge_sample(models.Model):
    Name = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.FileField(null=True,blank=True,upload_to='pics/')
    file = models.FileField(null=True,blank=True,upload_to='documents/')
    created_date = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    full_name = str(User.first_name) + str(User.last_name)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,default='Admin',null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name

