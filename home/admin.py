from django.contrib import admin
from .models import Time , Operation , OperationSetting ,User
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'status_date', 'start_session','volume','unit', )
    search_fields = ('username', 'phone_number')
    list_filter = (('status_date', JDateFieldListFilter), 'start_session')
    ordering = ('status_date',)



@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['operation_name', ]
    search_fields = ['operation_name',]


@admin.register(OperationSetting)
class OperationSettingAdmin(admin.ModelAdmin):
    list_display = ['Product', 'capacity_materials','unit_capacity','display_calculation', ]
    readonly_fields = ('display_calculation',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number' ]