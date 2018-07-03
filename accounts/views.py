from django.shortcuts import render
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def get_home(request): 
    return render(request, 'index.html')
    
def get_login(request):
    forms = UserLoginForm(request.POST)
    return render(request, 'accounts/login.html', {'forms': forms})
    
def register_seller(request): 
    forms = UserRegistrationForm(request.POST)
    return render(request, 'accounts/register.html', {'forms':forms})