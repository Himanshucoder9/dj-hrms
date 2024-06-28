from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Company)
admin.site.register(CompanyType)
admin.site.register(User)
admin.site.register(Staff)
admin.site.register(Education)

# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     model = User
#     resource_class = User
#     fieldsets = (
#         ('User Info', {
#             'fields': (
#                 'role', 'name', 'email', 'phone', 'dob', 'gender', 'profile', 'password'),
#         }),
#
#         ('Status', {
#             'fields': (
#                 'is_superuser', 'is_staff', 'is_active', 'is_verified',),
#         }),
#
#         ('Login Info', {
#             'fields': ('last_login', 'date_joined', 'groups', 'user_permissions'),
#         }),
#
#     )
#
#     def _profile(self, obj):
#         if obj.profile:
#             return format_html(
#                 '<img src="{}" style="max-width:50px; max-height:50px; border-radius:50%;"/>'.format(obj.profile.url))
#         else:
#             return "No Profile"
#
#     _profile.short_description = 'Profile'
#
#     list_display = (
#         'name', 'phone', 'email', 'gender', '_profile', 'role', 'is_verified', 'date_joined',)
#     list_filter = ('name', 'email', 'gender', 'phone', 'is_verified', 'role',)
#     readonly_fields = ('last_login', 'date_joined',)
#     search_fields = ('name', 'email', 'phone', 'role',)
#     add_fieldsets = (
#         (None, {
#             'fields': (
#                 'name', 'email', 'phone', 'dob', 'gender', 'profile', 'role', 'password1', 'password2',)}
#          ),
#     )
#     ordering = ('email',)
#     list_per_page = 10
#
#     def save_model(self, request, obj, form, change):
#         if not change:  # This is a new user
#             if obj.role == User.SUPERUSER:
#                 obj.is_staff = True
#                 obj.is_active = True
#                 obj.is_verified = True
#                 obj.is_superuser = True
#
#         else:  # This is an existing user
#             if obj.role == User.SUPERUSER:
#                 obj.is_staff = True
#                 obj.is_active = True
#                 obj.is_verified = True
#                 obj.is_superuser = True
#             else:
#                 # obj.is_staff = False
#                 obj.is_superuser = False
#         obj.save()
