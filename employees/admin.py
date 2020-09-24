from django.contrib import admin
from .models import Employee, AvailableJobs


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['First_Name', 'Last_Name', 'Email_id']	


@admin.register(AvailableJobs)
class AvailableJobsAdmin(admin.ModelAdmin):
	list_display = ['name']