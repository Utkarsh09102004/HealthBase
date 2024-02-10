# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('login/', patient_login, name='login'),
    path('', patient_home , name='home'),
    path('doctor-dashboard/', doctor_home, name='doctor-dashboard'),
    path('patient-dashboard/', patient_home, name="patient-dashboard"),
    path('user-data/', user_data , name='user-data'),
    path('audio/', audio_shit, name='audio')
    # Other URLs
]
