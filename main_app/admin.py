from django.contrib import admin
from .models import Make
from .models import CarModel
# Register your models here.
admin.site.register(Make)
admin.site.register(CarModel)
