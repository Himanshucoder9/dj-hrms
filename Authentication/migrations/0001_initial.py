# Generated by Django 5.0.6 on 2024-07-01 10:27

import Master.uploader
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('General', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Accountant', 'Accountant'), ('Manager', 'Manager'), ('HR', 'Human Resources'), ('Sales', 'Sales'), ('Employee', 'Employee')], default='Employee', max_length=50, verbose_name='Role')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('phone', models.CharField(help_text='Alphabets and special characters are not allowed (eg.+911234567890).', max_length=13, validators=[django.core.validators.RegexValidator(code='invalid_mobile_format', message='Mobile number must be in the format "+911234567890".', regex='^\\+\\d{1,13}$')], verbose_name='Mobile Number')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, verbose_name='Gender')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('company_code', models.CharField(max_length=6, unique=True, verbose_name='Company Code')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Company Name')),
                ('registered_office_address', models.TextField(verbose_name='Registered Office Address')),
                ('company_logo', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=Master.uploader.company_directory_path)),
                ('company_prefix', models.CharField(max_length=5, unique=True, verbose_name='Company Prefix')),
                ('company_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='General.companytype', verbose_name='Company Type')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to=Master.uploader.staff_directory_path)),
                ('staff_id', models.CharField(max_length=255, unique=True, verbose_name='Staff ID')),
                ('alt_phone', models.CharField(blank=True, help_text='Alphabets and special characters are not allowed (eg.+911234567890).', max_length=13, null=True, validators=[django.core.validators.RegexValidator(code='invalid_mobile_format', message='Mobile number must be in the format "+911234567890".', regex='^\\+\\d{1,13}$')], verbose_name='Emergency Mobile Number')),
                ('photo', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=Master.uploader.staff_directory_path)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Separated', 'Separated'), ('Widowed', 'Widowed'), ('Not Specified', 'Not Specified')], max_length=50, verbose_name='Marital Status')),
                ('father_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Father Name')),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mother Name')),
                ('joining_date', models.DateField(blank=True, null=True, verbose_name='Joining Date')),
                ('contract_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('internship', 'Internship'), ('freelance', 'Freelance'), ('other', 'Other')], max_length=50, verbose_name='Contract Type')),
                ('contract_start_date', models.DateField(blank=True, null=True, verbose_name='Contract Start Date')),
                ('contract_end_date', models.DateField(blank=True, null=True, verbose_name='Contract End Date')),
                ('experience', models.CharField(blank=True, max_length=50, null=True, verbose_name='Experience')),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O-', 'O-'), ('O+', 'O+'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=50, null=True, verbose_name='Blood Group')),
                ('current_address', models.TextField(verbose_name='Current Address')),
                ('permanent_address', models.TextField(verbose_name='Permanent Address')),
                ('is_handicapped', models.BooleanField(default=False, verbose_name='Is Handicapped')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.department', verbose_name='Department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.designation', verbose_name='Designation')),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staffs',
            },
            bases=('Authentication.user', models.Model),
        ),
    ]
