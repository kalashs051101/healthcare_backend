from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Patient, Doctor, PatientDoctorMapping


# Custom UserAdmin for our custom User model
class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'username', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    filter_horizontal = ('groups', 'user_permissions',)


# Custom PatientAdmin
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'address', 'user']
    search_fields = ['name', 'address']
    list_filter = ['age', 'user']
    ordering = ['name']


# Custom DoctorAdmin
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'specialization']
    search_fields = ['name', 'specialization']
    list_filter = ['specialization']
    ordering = ['name']


# Custom PatientDoctorMappingAdmin
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor']
    search_fields = ['patient__name', 'doctor__name']
    list_filter = ['doctor']
    ordering = ['patient']


# Register all models and their admins
admin.site.register(User, UserAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(PatientDoctorMapping, PatientDoctorMappingAdmin)
