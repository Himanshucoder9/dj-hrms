from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Employee

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, company_code=None, staff_id=None, password=None, **kwargs):
        try:
            if company_code and staff_id:
                employee = Employee.objects.get(company__company_code=company_code, staff_id=staff_id)
                if check_password(password, employee.password):
                    return employee
            else:
                # Handle superuser authentication
                email = kwargs.get('email')
                if email:
                    user = Employee.objects.get(email=email, is_superuser=True)
                    if check_password(password, user.password):
                        return user
        except Employee.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employee.objects.get(pk=user_id)
        except Employee.DoesNotExist:
            return None
