from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template.response import SimpleTemplateResponse
from datetime import date, datetime
from .models import UserDetails
from django.contrib.auth.views  import LoginView
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

class Login(LoginView):
    
    template_name = 'Login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SignUpView(FormView):
    template_name = 'CreateAccount.html'
    form_class = UserCreationForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = AuthenticationForm()
        return context

class HomeView(TemplateView):

    template_name = 'Home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context