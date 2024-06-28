from django.contrib import admin
from .models import *

admin.site.register(User)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_code', 'name', 'company_type', 'registered_office_address')
    search_fields = ('company_code', 'name')
    readonly_fields = ('company_code',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id',)
    readonly_fields = ('staff_id',)
