from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(models.Manager):
    def get_by_aadhar_number(self, aadhar_number):
        try:
            return self.get(aadhar_number=aadhar_number)
        except self.model.DoesNotExist:
            return None
class CustomUser(AbstractUser):
    aadhar_number = models.CharField(max_length=12)
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
    date_of_creation = models.DateTimeField(auto_now_add=True)
    medical_advice = models.CharField(max_length=500)
    body_temperature = models.CharField(max_length=30)
    medicine_list = models.CharField(max_length=500)
    reason_for_visit = models.CharField(max_length=500)
    blood_pressure = models.CharField(max_length=100)

    def __str__(self):
        return f"Prescription for {self.patient}"

class Audio_store(models.Model):
    record = models.FileField(upload_to='documents/')
    prescription = models.OneToOneField(Prescription, on_delete=models.CASCADE, related_name='audio_store')
