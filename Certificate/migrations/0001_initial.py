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
            name='IDCARD',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('issue_date', models.DateField(verbose_name='Issue Date')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.staff', verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'ID Card',
                'verbose_name_plural': 'ID Cards',
            },
        ),
    ]
