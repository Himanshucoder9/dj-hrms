from django.db import models
from django.utils.translation import gettext_lazy as _
from Master.models import TimeStamp
from Master.myvalidator import mobile_validator
from Master.uploader import stock_directory_path
from django.core.validators import FileExtensionValidator
import barcode
from barcode.writer import ImageWriter
import os
from django.conf import settings



# Create your models here.
class ItemCategory(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    name = models.CharField(_("Name"), max_length=255, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<ItemCategory(name={self.name})>"

    class Meta:
        verbose_name = _("Item Category")
        verbose_name_plural = _("Item Categories")


class ItemUnit(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    name = models.CharField(_("Name"), max_length=255, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<ItemUnit(name={self.name})>"

    class Meta:
        verbose_name = _("Item Unit")
        verbose_name_plural = _("Item Units")


class Shop(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    name = models.CharField(_("Shop Name"), max_length=255)
    phone = models.CharField(
        _("Shop Mobile Number"),
        max_length=13,
        validators=[mobile_validator],
        help_text="Alphabets and special characters are not allowed (eg.+911234567890).",
    )
    email = models.EmailField(_("Shop Email"), max_length=255, blank=True, null=True)
    address = models.TextField(_("Shop Address"), blank=True, null=True)
    supplier_name = models.CharField(_("Supplier Name"), max_length=255)
    supplier_phone = models.CharField(
        _("Supplier Mobile Number"),
        max_length=13,
        validators=[mobile_validator],
        help_text="Alphabets and special characters are not allowed (eg.+911234567890).",
    )
    supplier_email = models.EmailField(_("Supplier Email"), max_length=255, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Shop(name={self.name})>"

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")


class Item(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    name = models.CharField(_("Name"), max_length=255)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, verbose_name=_('Category'))
    unit = models.ForeignKey(ItemUnit, on_delete=models.CASCADE, verbose_name=_('Unit'))
    description = models.TextField(_("Description"), blank=True, null=True)
    barcode = models.CharField(_("Barcode"), max_length=255, unique=True, blank=True, null=True)
    barcode_image = models.ImageField(_("Barcode Image"), upload_to='barcodes/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    def __repr__(self):
        return f"<Item(name={self.name})>"

    
    def save(self, *args, **kwargs):
        if not self.barcode:
            self.barcode = self.generate_unique_barcode()
        if not self.barcode_image:
            self.barcode_image = self.generate_barcode_image()
        super().save(*args, **kwargs)

    def generate_unique_barcode(self):
        EAN = barcode.get_barcode_class('ean13')
        unique = False
        while not unique:
            barcode_number = f'{self.company.company_code}{self.id or 0:06d}'.zfill(12)
            if not Item.objects.filter(barcode=barcode_number).exists():
                unique = True
        return barcode_number

    def generate_barcode_image(self):
        EAN = barcode.get_barcode_class('ean13')
        barcode_number = self.barcode
        ean = EAN(barcode_number, writer=ImageWriter())
        directory = os.path.join(settings.MEDIA_ROOT, f'{self.company.company_code}/stocks/barcodes')
        print(self.company.company_code)
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f'{barcode_number}'
        full_path = os.path.join(directory, filename)
        ean.save(full_path)
        relative_path = os.path.relpath(full_path, settings.MEDIA_ROOT)
        return f'{relative_path}.png'
    
    def __str__(self):
        return f'name-{self.name},category.{self.category.name}'

    def __repr__(self):
        return f"<Item(name={self.name})>"

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")


class ItemOrder(TimeStamp):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('cancel', 'Cancel'),
        ('received', 'Received')
    )
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=_('Item'))
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name=_('Shop'))
    quantity = models.PositiveIntegerField(_("Quantity"), default=0)
    unit_price = models.PositiveIntegerField(_("Unit Price"), default=0)
    total_amount = models.PositiveIntegerField(_("Total Amount"), default=0)
    bill = models.FileField(
        verbose_name=_("Bill"),
        upload_to=stock_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload document..", blank=True, null=True)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')

    def __str__(self):
        return f'name-{self.item.name},shop.{self.shop.name}'

    def __repr__(self):
        return f"<ItemOrder(name={self.item.name})>"

    class Meta:
        verbose_name = _("Item Order")
        verbose_name_plural = _("Item Orders")


class ItemStock(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=_('Item'))
    stock_quantity = models.PositiveIntegerField(_("Stock Quantity"), default=0)
    reorder_level = models.PositiveIntegerField(_("Reorder Level"), default=10)

    def __str__(self):
        return f'name-{self.item.name}'

    def __repr__(self):
        return f"<ItemStock(name={self.item.name})>"

    class Meta:
        verbose_name = _("Item Stock")
        verbose_name_plural = _("Item Stocks")


class ItemIssued(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=_('Item'))
    in_quantity = models.PositiveIntegerField(_("In Quantity"), default=0)
    out_quantity = models.PositiveIntegerField(_("Out Quantity"), default=0)
    issued_to = models.ForeignKey('Authentication.Staff', on_delete=models.CASCADE, related_name='issued_items',
                                  verbose_name=_('Issued to'))
    issued_by = models.ForeignKey('Authentication.Staff', on_delete=models.CASCADE, related_name='issued_by_items',
                                  verbose_name=_('Issued by'))
    issued_date = models.DateTimeField(_("Issued Date"))
    return_date = models.DateTimeField(_("Return Date"), blank=True, null=True)
    note = models.TextField(_("Note"), blank=True, null=True)

    def __str__(self):
        return f'name-{self.item.name}'

    def __repr__(self):
        return f"<ItemIssued(name={self.item.name})>"

    class Meta:
        verbose_name = _("Item Issued")
        verbose_name_plural = _("Item Issues")
