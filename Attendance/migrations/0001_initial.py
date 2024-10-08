# Generated by Django 5.0.6 on 2024-07-04 08:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('check_in', models.DateTimeField(blank=True, null=True, verbose_name='Check In')),
                ('check_out', models.DateTimeField(blank=True, null=True, verbose_name='Check Out')),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late'), ('half_day', 'Half Day'), ('on_leave', 'On Leave'), ('holiday', 'Holiday')], max_length=20, verbose_name='Status')),
                ('hours_worked', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Hours Worked')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
            },
        ),
        migrations.CreateModel(
            name='Break',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
            ],
            options={
                'verbose_name': 'Break',
                'verbose_name_plural': 'Breaks',
            },
        ),
        migrations.CreateModel(
            name='BreakType',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Break Type',
                'verbose_name_plural': 'Break Types',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('date', models.DateField(verbose_name='Date')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Holiday',
                'verbose_name_plural': 'Holidays',
            },
        ),
        migrations.CreateModel(
            name='LeaveRecord',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('from_date', models.DateField(verbose_name='From Date')),
                ('to_date', models.DateField(verbose_name='To Date')),
                ('reason', models.TextField(verbose_name='Reason')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20, verbose_name='Status')),
                ('reject_reason', models.TextField(blank=True, null=True, verbose_name='Reject Reason')),
            ],
            options={
                'verbose_name': 'Leave Record',
                'verbose_name_plural': 'Leave Records',
            },
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Leave Type',
                'verbose_name_plural': 'Leave Types',
            },
        ),
    ]
