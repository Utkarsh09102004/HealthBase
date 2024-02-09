from django.shortcuts import render

# Create your views here.

def Patient_login(request):

    return render(request, 'base/patient_login.html')