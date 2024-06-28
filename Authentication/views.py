from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .backends import CustomAuthBackend
from .models import Employee
from .forms import EmployeeLoginForm


def login_view(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            company_code = form.cleaned_data['company_code']
            staff_id = form.cleaned_data['staff_id']
            password = form.cleaned_data['password']

            user = CustomAuthBackend().authenticate(request, company_code=company_code, staff_id=staff_id, password=password)
            if user is not None:
                login(request, user, backend='Authentication.backends.CustomAuthBackend')
                return redirect('some_view')  # Redirect to a success page.
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = EmployeeLoginForm()

    return render(request, 'auth/login.html', {'form': form})
