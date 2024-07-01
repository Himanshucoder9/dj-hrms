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


def staff_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/staffs/{filename}'


def staff_doc_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/staffs/docs/{filename}'


def staff_bank_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/staffs/bank/{filename}'


def stock_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/stocks/order/{filename}'

def stock_barcode_directory_path(instance, filename):
    company_code = slugify(instance.company.company_code)
    return f'company_data/{company_code}/stocks/barcodes/{filename}'