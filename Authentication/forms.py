from django import forms


class EmployeeLoginForm(forms.Form):
    company_code = forms.CharField(max_length=50)
    staff_id = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
