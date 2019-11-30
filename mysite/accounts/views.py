from django.shortcuts import render,redirect

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Student
from .forms import UserForm,ProfileForm
from django.core.mail import send_mail
#from django.shortcuts import decorator


User = get_user_model()
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('profile')
        else:
            messages.error(request,'Invalid Email or Password')
            return redirect('login')
    else:
        return render(request,'login1.html')

def register(request):
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    return render(request,'profile.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        regdno = request.POST['regdno']

        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.warning(request,'Email already exists')
                return redirect('register')
            elif User.objects.filter(regdno = regdno).exists():
                messages.warning(request,'Registration number already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password1,regdno=regdno)
                user.save()
                user = auth.authenticate(email=email,password=password1)
                if user is not None:
                    auth.login(request,user)
                messages.success(request,'User is Created , PLEASE WAIT TILL ADMIN APPROVE YOU TO ACCESS')
                return render(request,'user_fill.html',{'user':user})
        else:
            messages.warning(request,'Password and Confirm password not match')
            return redirect('register')

    else:
        return render(request,'register.html')

def admin_page(request):
    return render(request,'admin_page.html')

def user_fill(request):
    return render(request,'user_fill.html')

def user_data(request,regdno):
    if request.method == 'POST':

       # form = ImageUploadForm(request.POST,request.FILES)
        gender = request.POST['gender']
        phoneno = request.POST['phoneno']
        dob = request.POST['dob']
       # profile_image = request.FILES['profile_image']
        college = request.POST['college']
        branch = request.POST['branch']

      #  form = ProfileForm(request.POST,request.FILES)
      #  if form.is_valid():
      #      img = Student(profile_image=request.FILES['image'])
      #      img.save()

        request.user.gender = gender
        request.user.phoneno = phoneno
        request.user.dob = dob
       # request.user.profile_image = request.FILES['profile_image']
        request.user.college = college
        request.user.branch = branch


        form = UserForm(request.POST, request.FILES or None,instance = request.user)
        if form.is_valid():
            img = UserForm(profile_image=request.FILES['profile_image'])
           # return redirect('profile')
           # return redirect('profile')
        else:
            form = UserForm(instance = request.user)

        request.user.save()

        '''MyProfileForm = ProfileForm(request.POST,request.FILES)
        if MyProfileForm.is_valid():
            student = Student()
            student.profile_image = MyProfileForm.cleaned_data['profile_image']
            student.save() '''

        ''' form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            m = Student.objects.get(regdno = regdno )
            m.profile_image = form.cleaned_data['profile_image']
            m.save() '''

        send_mail('TheLearner CreateUser',"'Dear' +request.user.first_name + 'you have successfully Registered with TheLearner , Please wait till admin Approves you '",'thelearnercse123@gmail.com',[request.user.email])
        return redirect('/')
    else:
        return redirect('/')

def edit_profile(request):

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES or None,instance = request.user)
        if form.is_valid():
            request.user.save()
           # return redirect('profile')
            return redirect('profile')
    else:
        form = UserForm(instance = request.user)
    return render(request,'edit_profile.html',{'form':form})

def admin_page(request):
    return render(request,'admin_page.html')

def user_draft(request):

    users = User.objects.filter(date_of_approved__isnull=True).order_by('-date_of_join')
    return render(request,'user_draft.html',{'users':users})

def approve(request,regdno):
    user = User.objects.get(regdno=regdno)
    #print(user.first_name)
    #print(user.approve())
    user.approve()
    user.save()
    return redirect('user_draft')

def delete(request,regdno):
    user = User.objects.get(regdno=regdno)
    #print(user.last_name)
    user.delete()
    return redirect('user_draft')