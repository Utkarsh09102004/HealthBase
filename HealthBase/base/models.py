from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    aadhar_number = models.CharField(max_length=12, unique=True)
    phone_number = models.CharField(max_length=15)
    DOCTOR = 'doctor'
    PATIENT = 'patient'
    ROLE_CHOICES = [
        (DOCTOR, 'Doctor'),
        (PATIENT, 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=PATIENT)

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
