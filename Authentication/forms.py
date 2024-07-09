from django import forms

from Authentication.models import Staff, Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('created_at', 'updated_at')

        widgets = {
            'company_code': forms.TextInput(attrs={'readonly': 'true'}),
            'company_logo': forms.ClearableFileInput(attrs={'class': 'form-control imageInput'}),
        }


class StaffLoginForm(forms.Form):
    company_code = forms.CharField(max_length=50)
    staff_id = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ('staff_id', 'company', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined',
                   'groups',
                   'user_permissions', 'password', 'qr_code')
