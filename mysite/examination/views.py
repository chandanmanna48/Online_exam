from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import GeneralKnowledge,Add_GeneralKnowledge_sample


# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

#def login(request):

   # return render(request,'login1.html')



def aptitude(request):
    return render(request,'aptitude.html')

def reasogning(request):
    return render(request,'reasogning.html')

def gk(request):
    return render(request,'GeneralKnowledge_base.html')

def sample_practice_gk(request):

    objs = Add_GeneralKnowledge_sample.objects.order_by('-created_date')
    return render(request,'generalknowledge_sample_practice.html',{'objs':objs})

def online_test_gk(request):
    objs = GeneralKnowledge.objects.all()
    return render(request,'GeneralKnowledge_test.html',{'objs':objs})

def GeneralKnowledge_result(request):
    objs = GeneralKnowledge.objects.all()
    count = 0


    for obj in objs:
        var = request.POST[str(obj.qno)]
        obj.user_select = var
        
        if obj.answer == var:
            count += 1

    total = len(objs)
    percent = int((count / total) * 100)

    if percent >= 85:
        message = ' You are doing well '
    else:
        message = 'Try best next time'
    return render(request,'GeneralKnowledge_result.html',{'objs':objs,'total':total,'percent':percent,'count':count,'message':message})

def sample_practice_aptitude(request):

    return render(request,'aptitude_sample_practice.html')

def online_test_aptitude(request):
    return render(request,'aptitude_test.html')

def aptitude_result(request):
    return render(request,'aptutude_result.html')

def sample_practice_reasogning(request):
    pass

def online_test_reasogning(request):
    pass

def reasogning_result(request):
    pass