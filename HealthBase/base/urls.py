# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('login/', patient_login, name='login'),
    path('', patient_home , name='home'),
    # Other URLs
]
