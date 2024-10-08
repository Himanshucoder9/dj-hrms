from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from Master.models import TimeStamp
from Master.myvalidator import alphanumeric, alphabet
from imagekit.models import ProcessedImageField
from Master.uploader import expense_directory_path
import uuid


# Create your models here.

class Head(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    expense_head = models.CharField(_("expense head"), max_length=250, validators=[alphanumeric('Expense head')])
    note = models.TextField(_("note"), blank=True, null=True)

    def __str__(self):
        return self.expense_head

    def __repr__(self):
        return f"<Head(expense_head={self.expense_head})>"

    class Meta:
        verbose_name = _("Head")
        verbose_name_plural = _("Heads")


class Expense(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    expense_head = models.ForeignKey(Head, on_delete=models.CASCADE, verbose_name="Expense head")
    name = models.CharField(_("name"), max_length=250, validators=[alphabet('Name')])
    invoice_no = models.CharField(_("invoice number"), max_length=300, blank=True, null=True,
                                  validators=[alphanumeric('Invoice number')])
    date = models.DateField(_("date"))
    amount = models.DecimalField(_("amount"), max_digits=10, decimal_places=2)
    bill = models.FileField(
        verbose_name=_("Bill"),
        upload_to=expense_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload document..", blank=True, null=True)
    note = models.TextField(_("note"), blank=True, null=True)
    is_paid = models.BooleanField(_("is paid"), default=False)

    class Meta:
        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Expense(name={self.name})>"
