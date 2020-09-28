from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import employee

@admin.register(employee)
class employeeAdmin(ImportExportModelAdmin):
    pass



# Register your models here.
