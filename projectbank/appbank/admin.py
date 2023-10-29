from django.contrib import admin
from .models import Branch
from .models import Applicant

# Register your models here.

admin.site.register(Branch)
admin.site.register(Applicant)
