
# views.py
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
from django.http import HttpResponse
from .forms import *
from .audioScript import sum_gen



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
                return redirect('doctor-dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'base/patient_login.html')


def doctor_home(request):
    if request.method == 'POST':
        aadhar_number = request.POST.get('aadhar_number')

        users = CustomUser.objects.filter(aadhar_number=aadhar_number).first()
        if users:
            request.session['data'] = aadhar_number

        else:
            messages.error(request, 'Incorrect Aadhar number.')


    return render(request, 'base/doctor_home.html')


from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AudioForm
from .models import Audio_store, Patient

from django.shortcuts import render, redirect
from .forms import AudioForm
from .models import Patient, CustomUser, Prescription
import os


def user_data(request):
    data = request.session.get('data')
    user = CustomUser.objects.get(aadhar_number=data)
    context = {'user': user}

    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
        else:
            form = AudioForm()
    return render(request, 'base/user-data.html', {'form': form})

from django.conf import settings
def audio_shit(request):
    dict= sum_gen(os.path.join(settings.MEDIA_ROOT, 'documents', 'doct.mp3'))
    context = {'dict': dict}
    user = CustomUser.objects.get(aadhar_number='867056273281')


    prescription = Prescription(
        patient=patient,
        medical_advice=dict['advice'],
        body_temperature=dict['temp'],
        medicine_list=dict['medicine'],
        reason_for_visit=dict['reason'],
        blood_pressure=dict['bp']
    )
    prescription.save()
    return render(request, 'base/success.html',context)

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def patient_home(request):
    return render(request, 'base/patient_home.html')