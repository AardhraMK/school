from django.contrib import admin # type: ignore
from schoolapp.models import *

# Register your models here.
admin.site.register(School)
admin.site.register(Batch)
admin.site.register(Student)