from django import forms
from General.models import CompanyType, Designation, Department


class CompanyTypeForm(forms.ModelForm):
    class Meta:
        model = CompanyType
        fields = ('name',)


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ('name',)


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name',)
