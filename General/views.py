from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from General.forms import CompanyTypeForm
from General.models import CompanyType
from Authentication.forms import CompanyForm
from Authentication.models import Company

def companyDashboard(request):
    return render(request, 'pages/dashboard.html')


class CompanyTypeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'general/company_type.html'
    success_url = reverse_lazy('general:company_type_detail')
    form_class = CompanyTypeForm
    model = CompanyType
    success_message = "Company Type was created successfully"


class CompanyTypeListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    template_name = 'general/company_type_detail.html'
    context_object_name = "list"
    model = CompanyType


class CompanyTypeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'general/company_type.html'
    success_url = reverse_lazy('general:company_type_detail')
    form_class = CompanyTypeForm
    model = CompanyType
    success_message = "Company Type was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        context['update_id'] = self.object.id
        context['update_url'] = 'company_type_update'
        return context


@login_required(login_url='login')
def companyTypeDelete(request, id):
    classes = CompanyType.objects.get(id=id)
    classes.delete()
    messages.add_message(request, messages.SUCCESS, "Company Type was deleted successfully")
    return redirect(reverse('general:company_type_list'))

class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'general/company_detail.html'
    context_object_name = 'company'

    def get_object(self):
        return self.request.user.company

class CompanyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'general/company.html'
    success_url = reverse_lazy('general:company_detail')
    form_class = CompanyForm
    model = Company
    success_message = "Company was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        context['update_id'] = self.object.id
        context['company_logo'] = self.object.company_logo
        context['update_url'] = 'company_update'
        return context

