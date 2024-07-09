from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from Authentication.models import Staff


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, company_code=None, staff_id=None, password=None, **kwargs):
        try:
            if company_code and staff_id:
                staff = Staff.objects.get(company__company_code=company_code, staff_id=staff_id)
                if check_password(password, staff.password):
                    return staff
            else:
                # Handle superuser auth
                email = kwargs.get('email')
                if email:
                    user = Staff.objects.get(email=email, is_superuser=True)
                    if check_password(password, user.password):
                        return user
        except Staff.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Staff.objects.get(pk=user_id)
        except Staff.DoesNotExist:
            return None
