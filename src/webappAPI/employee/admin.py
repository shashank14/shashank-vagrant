from django.contrib import admin

# Register your models here.

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):

    list_display = ['name', 'num','role']

    class Meta:
        model = Employee

admin.site.register(Employee,EmployeeAdmin)
