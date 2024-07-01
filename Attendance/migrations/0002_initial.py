# Generated by Django 5.0.6 on 2024-07-01 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Attendance', '0001_initial'),
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.staff', verbose_name='Staff'),
        ),
        migrations.AddField(
            model_name='break',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='break',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.staff', verbose_name='Staff'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='breaks',
            field=models.ManyToManyField(blank=True, null=True, to='Attendance.break', verbose_name='Breaks'),
        ),
        migrations.AddField(
            model_name='breaktype',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='break',
            name='break_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Attendance.breaktype', verbose_name='Break Type'),
        ),
        migrations.AddField(
            model_name='holiday',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='leaverecord',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='leaverecord',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.staff', verbose_name='Staff'),
        ),
        migrations.AddField(
            model_name='leavetype',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='leaverecord',
            name='leave_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Attendance.leavetype', verbose_name='Leave Type'),
        ),
    ]
