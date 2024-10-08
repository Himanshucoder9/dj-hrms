# Generated by Django 5.0.6 on 2024-07-04 08:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayrollPeriod',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('is_locked', models.BooleanField(default=False, verbose_name='Is Locked')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Payroll Period',
                'verbose_name_plural': 'Payroll Periods',
            },
        ),
        migrations.CreateModel(
            name='PayrollReport',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('payroll_period', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Payroll.payrollperiod', verbose_name='Payroll Period')),
                ('total_basic_salary', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total Basic Salary')),
                ('total_hra', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total HRA')),
                ('total_conveyance', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total Conveyance')),
                ('total_medical_allowance', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total Medical Allowance')),
                ('total_special_allowance', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total Special Allowance')),
                ('total_epf_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total EPF Contribution')),
                ('total_esi_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total ESI Contribution')),
                ('total_professional_tax', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total Professional Tax')),
                ('total_tds', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total TDS')),
                ('total_net_salary', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total Net Salary')),
            ],
            options={
                'verbose_name': 'Payroll Report',
                'verbose_name_plural': 'Payroll Reports',
            },
        ),
        migrations.CreateModel(
            name='PayrollEntry',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Basic Salary')),
                ('hra', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='House Rent Allowance (HRA)')),
                ('conveyance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Conveyance Allowance')),
                ('medical_allowance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Medical Allowance')),
                ('special_allowance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Special Allowance')),
                ('epf_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='EPF Contribution')),
                ('esi_contribution', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='ESI Contribution')),
                ('professional_tax', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Professional Tax')),
                ('tds', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Tax Deducted at Source (TDS)')),
                ('net_salary', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Net Salary')),
                ('overtime_hours', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Overtime Hours')),
                ('bonus', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Bonus')),
                ('penalties', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Penalties')),
                ('other_allowances', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Other Allowances')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.staff', verbose_name='Staff')),
                ('payroll_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Payroll.payrollperiod', verbose_name='Payroll Period')),
            ],
            options={
                'verbose_name': 'Payroll Entry',
                'verbose_name_plural': 'Payroll Entries',
            },
        ),
        migrations.CreateModel(
            name='PayrollAdjustment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('reason', models.TextField(verbose_name='Reason')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.staff', verbose_name='Staff')),
                ('payroll_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Payroll.payrollperiod', verbose_name='Payroll Period')),
            ],
            options={
                'verbose_name': 'Payroll Adjustment',
                'verbose_name_plural': 'Payroll Adjustments',
            },
        ),
        migrations.CreateModel(
            name='StaffBasicPayroll',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Basic Salary')),
                ('hra', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='House Rent Allowance (HRA)')),
                ('conveyance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Conveyance Allowance')),
                ('medical_allowance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Medical Allowance')),
                ('special_allowance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Special Allowance')),
                ('epf_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='EPF Number')),
                ('esi_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='ESI Number')),
                ('professional_tax', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Professional Tax')),
                ('tds', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Tax Deducted at Source (TDS)')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.staff', verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'Staff Basic Payroll',
                'verbose_name_plural': 'Staff Basic Payrolls',
            },
        ),
    ]
