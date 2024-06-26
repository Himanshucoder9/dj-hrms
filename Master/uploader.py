from django.utils.text import slugify
import os


def company_directory_path(instance, filename):
    company_code = slugify(instance.company_code)
    return f'company_data/{company_code}/{filename}'


def expense_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/expenses/{filename}'


def account_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/accounts/{filename}'


def achievement_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/achievements/{filename}'


def employee_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/employees/{filename}'


def employee_doc_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/employees/docs/{filename}'


def employee_bank_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/employees/bank/{filename}'
