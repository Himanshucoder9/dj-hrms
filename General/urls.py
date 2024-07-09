from django.urls import path
from General.views import CompanyTypeListView, CompanyTypeCreateView, CompanyTypeUpdateView, companyTypeDelete,CompanyUpdateView, companyDashboard

app_name = 'general'

urlpatterns = [
    #Company Type
    path('', companyDashboard, name="dashboard"),
    path('company-type/add/', CompanyTypeCreateView.as_view(), name="company_type_add"),
    path('company-type/detail/', CompanyTypeListView.as_view(), name="company_type_detail"),
    path('company-type/<uuid:pk>/update/', CompanyTypeUpdateView.as_view(), name="company_type_update"),
    path('company-type/<uuid:pk>/delete/', companyTypeDelete, name="company_type_delete"),
    #Company
    path('company/<uuid:pk>/update/', CompanyUpdateView.as_view(), name="company_update"),

]
