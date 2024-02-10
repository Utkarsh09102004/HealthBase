from django.contrib import admin
from .models import *




admin.site.register(CustomUser)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Prescription)
admin.site.register(Audio_store)
