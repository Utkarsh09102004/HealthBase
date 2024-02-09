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
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    age = models.PositiveIntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True, blank=True)




class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    medical_license_number = models.CharField(max_length=100)
    patients = models.ManyToManyField(Patient, related_name='doctors')


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)