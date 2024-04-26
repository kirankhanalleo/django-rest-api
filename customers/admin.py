from django.contrib import admin

from .models import Customers

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age','phone_numer']

admin.site.register(Customers,CustomerAdmin)