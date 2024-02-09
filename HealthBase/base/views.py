# accounts/views.py

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# views.py
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages



@csrf_exempt
def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'patient':
                return redirect('patient_dashboard')
            elif user.role == 'doctor':
                return redirect('doctor_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'base/patient_login.html')

def patient_home(request):
    return render(request, 'base/patient_home.html')


def patient_home(request):
    return render(request, 'base/patient_home.html')