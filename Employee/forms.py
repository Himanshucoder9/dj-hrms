from django import forms
from .models import *


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ('company', 'created_at', 'updated_at')
        # widgets = {
        #     'company': forms.HiddenInput(),
        # }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ('company', 'created_at', 'updated_at')


class BankDetailForm(forms.ModelForm):
    class Meta:
        model = BankDetail
        fields = '__all__'
        exclude = ('company', 'created_at', 'updated_at')


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = '__all__'
        exclude = ('company', 'created_at', 'updated_at')


