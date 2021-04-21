from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template.response import SimpleTemplateResponse
from datetime import date, datetime
from .models import UserDetails
from django.views.decorators.csrf import csrf_protect,csrf_exempt

# Create your views here.

def home(request):
    response = SimpleTemplateResponse('Home.html')
    return response

def get_current_time(request):
    current_time = datetime.now()
    timezone = request.GET.get('timezone')
    
    context = {
        'current_time' : current_time,
        'timezone' : timezone
    }
    
    response = SimpleTemplateResponse('current_time.html',context)
    return response

def login(request):
    response = SimpleTemplateResponse('Login.html')
    return response


def create_account(request):

    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('dateOfBirth') and request.POST.get('phone') and request.POST.get('username') and request.POST.get('password'):
                post=UserDetails()
                post.fname= request.POST.get('fname')
                post.lname= request.POST.get('lname')
                post.save()
                
        return render(request, 'CreateAccount.html')  

    else:
        return render(request,'CreateAccount.html')



def thanks(request):
    response = SimpleTemplateResponse('ThankYou_Registration.html')
    return response

def user_profile(request):
    response = SimpleTemplateResponse('UserProfile.html')
    return response

class HealthHome(View):
    def homepage(self, request):
        return HttpResponse('HealthHomePage')