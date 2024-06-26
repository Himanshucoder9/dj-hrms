from django.utils.text import slugify
import os


def company_directory_path(instance, filename):
    company_code = slugify(instance.company_code)
    return f'company_data/{company_code}/{filename}'


def expense_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/expenses/{filename}'