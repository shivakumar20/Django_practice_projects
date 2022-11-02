from django.contrib import admin

from home.models import Department, Employee, Role

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)