from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from Authentication.backends import CustomAuthBackend
from Authentication.models import Staff
from Authentication.forms import StaffLoginForm
from django.forms import inlineformset_factory
from Authentication.models import Staff
from Employee.models import Education, Document, BankDetail, SocialMedia
from .forms import StaffForm
from Employee.forms import EducationForm, DocumentForm, BankDetailForm, SocialMediaForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            company_code = form.cleaned_data['company_code']
            staff_id = form.cleaned_data['staff_id']
            password = form.cleaned_data['password']

            user = CustomAuthBackend().authenticate(request, company_code=company_code, staff_id=staff_id,
                                                    password=password)
            if user is not None:
                login(request, user, backend='Authentication.backends.CustomAuthBackend')
                return redirect('create_staff')  # Redirect to a success page.
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = StaffLoginForm()

    return render(request, 'auth/login.html', {'form': form})


@login_required
def create_staff(request):
    EducationFormSet = inlineformset_factory(Staff, Education, form=EducationForm, extra=1)
    DocumentFormSet = inlineformset_factory(Staff, Document, form=DocumentForm, extra=1)
    BankDetailFormSet = inlineformset_factory(Staff, BankDetail, form=BankDetailForm, extra=1)
    SocialMediaFormSet = inlineformset_factory(Staff, SocialMedia, form=SocialMediaForm, extra=1)

    user = request.user
    company = user.company  # Assuming the User model has a ForeignKey to the Company model

    if request.method == "POST":
        staff_form = StaffForm(request.POST, request.FILES)
        education_formset = EducationFormSet(request.POST, request.FILES)
        document_formset = DocumentFormSet(request.POST, request.FILES)
        bank_detail_formset = BankDetailFormSet(request.POST, request.FILES)
        social_media_formset = SocialMediaFormSet(request.POST, request.FILES)

        if (staff_form.is_valid() and education_formset.is_valid() and document_formset.is_valid() and
                bank_detail_formset.is_valid() and social_media_formset.is_valid()):
            staff = staff_form.save(commit=False)
            staff.company = company
            staff.save()

            # Save each formset with the staff instance and company field
            education_formset = EducationFormSet(request.POST, request.FILES, instance=staff)
            for form in education_formset:
                instance = form.save(commit=False)
                instance.company = company
                instance.save()

            document_formset = DocumentFormSet(request.POST, request.FILES, instance=staff)
            for form in document_formset:
                instance = form.save(commit=False)
                instance.company = company
                instance.save()

            bank_detail_formset = BankDetailFormSet(request.POST, request.FILES, instance=staff)
            for form in bank_detail_formset:
                instance = form.save(commit=False)
                instance.company = company
                instance.save()

            social_media_formset = SocialMediaFormSet(request.POST, request.FILES, instance=staff)
            for form in social_media_formset:
                instance = form.save(commit=False)
                instance.company = company
                instance.save()

            return redirect('some_success_url')
    else:
        staff_form = StaffForm(initial={'company': company})
        education_formset = EducationFormSet(instance=Staff())
        document_formset = DocumentFormSet(instance=Staff())
        bank_detail_formset = BankDetailFormSet(instance=Staff())
        social_media_formset = SocialMediaFormSet(instance=Staff())

    context = {
        'staff_form': staff_form,
        'education_formset': education_formset,
        'document_formset': document_formset,
        'bank_detail_formset': bank_detail_formset,
        'social_media_formset': social_media_formset,
    }
    return render(request, 'auth/test.html', context)