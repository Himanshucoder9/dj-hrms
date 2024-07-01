# Generated by Django 5.0.6 on 2024-07-01 10:27

import Master.uploader
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Item Category',
                'verbose_name_plural': 'Item Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('barcode', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Barcode')),
                ('barcode_image', models.ImageField(blank=True, null=True, upload_to='barcodes/', verbose_name='Barcode Image')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.itemcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='ItemIssued',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('issued_date', models.DateTimeField(verbose_name='Issued Date')),
                ('return_date', models.DateTimeField(blank=True, null=True, verbose_name='Return Date')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
                ('issued_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issued_by_items', to='Authentication.staff', verbose_name='Issued by')),
                ('issued_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issued_items', to='Authentication.staff', verbose_name='Issued to')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.item', verbose_name='Item')),
            ],
            options={
                'verbose_name': 'Item Issued',
                'verbose_name_plural': 'Item Issues',
            },
        ),
        migrations.CreateModel(
            name='ItemStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('stock_quantity', models.PositiveIntegerField(default=0, verbose_name='Stock Quantity')),
                ('reorder_level', models.PositiveIntegerField(default=10, verbose_name='Reorder Level')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.item', verbose_name='Item')),
            ],
            options={
                'verbose_name': 'Item Stock',
                'verbose_name_plural': 'Item Stocks',
            },
        ),
        migrations.CreateModel(
            name='ItemUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Item Unit',
                'verbose_name_plural': 'Item Units',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.itemunit', verbose_name='Unit'),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=255, verbose_name='Shop Name')),
                ('phone', models.CharField(help_text='Alphabets and special characters are not allowed (eg.+911234567890).', max_length=13, validators=[django.core.validators.RegexValidator(code='invalid_mobile_format', message='Mobile number must be in the format "+911234567890".', regex='^\\+\\d{1,13}$')], verbose_name='Shop Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Shop Email')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Shop Address')),
                ('supplier_name', models.CharField(max_length=255, verbose_name='Supplier Name')),
                ('supplier_phone', models.CharField(help_text='Alphabets and special characters are not allowed (eg.+911234567890).', max_length=13, validators=[django.core.validators.RegexValidator(code='invalid_mobile_format', message='Mobile number must be in the format "+911234567890".', regex='^\\+\\d{1,13}$')], verbose_name='Supplier Mobile Number')),
                ('supplier_email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Supplier Email')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
            },
        ),
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('unit_price', models.PositiveIntegerField(default=0, verbose_name='Unit Price')),
                ('total_amount', models.PositiveIntegerField(default=0, verbose_name='Total Amount')),
                ('bill', models.FileField(blank=True, help_text='Upload document..', null=True, upload_to=Master.uploader.stock_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])], verbose_name='Bill')),
                ('order_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('cancel', 'Cancel'), ('received', 'Received')], default='pending', max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.company', verbose_name='Company')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.item', verbose_name='Item')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.shop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': 'Item Order',
                'verbose_name_plural': 'Item Orders',
            },
        ),
    ]
