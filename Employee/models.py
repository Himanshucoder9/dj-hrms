from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from Authentication.models import Company, Staff
from Master.models import TimeStamp
from Master.myvalidator import mobile_validator, numeric, minimum, maximum, pan_validator
from imagekit.models import ProcessedImageField
from Master.uploader import staff_directory_path
import uuid


class Education(TimeStamp):
    EDUCATION_CHOICES = (
        ('10th', '10th'),
        ('12th', '12th'),
        ('UG', 'Under Graduation'),
        ('PG', 'Post Graduation'),
        ('Other', 'Other'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Company'))
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_('Staff'))
    education = models.CharField(verbose_name="Education Type", choices=EDUCATION_CHOICES, max_length=15, )
    score = models.CharField(_('Score'), max_length=50, )
    document = models.FileField(
        upload_to='auth/agent/education',
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload education certificate..", )

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class Document(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Company'))
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_('Staff'))
    aadhar_no = models.CharField(_("Aadhar Number"), max_length=12, null=True,
                                 validators=[numeric("Aadhar Number"), minimum(12, 'Aadhar '
                                                                                   'number'),
                                             maximum(12, 'Aadhar number')],
                                 help_text="Only numbers are allowed.")
    pan_no = models.CharField(_("Pan Number"), max_length=10, validators=[pan_validator])
    aadhar_document = models.FileField(
        verbose_name=_("Aadhar Document"),
        upload_to=staff_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload Aadhar card..", )
    pan_document = models.FileField(
        verbose_name=_("Pan Document"),
        upload_to=staff_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload Pan card..", )
    resume = models.FileField(
        verbose_name=_("Resume"),
        upload_to=staff_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload Resume..",
        blank=True, null=True)
    offer_letter = models.FileField(
        verbose_name=_("Offer Letter"),
        upload_to=staff_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload Offer Letter..",
        blank=True, null=True)
    joining_letter = models.FileField(
        verbose_name=_("Joining Letter"),
        upload_to=staff_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload Joining Letter..",
        blank=True, null=True)
    resignation_letter = models.FileField(
        verbose_name=_("Resignation Letter"),
        upload_to=staff_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload Resignation Letter..",
        blank=True, null=True)
    other_document = models.FileField(
        verbose_name=_("Other Document"),
        upload_to=staff_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload Other Document..",
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.staff.first_name}"

    def __repr__(self):
        return f"<Document(staff={self.staff})>"

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'


class BankDetail(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Company'))
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_('Staff'))
    account_holder_name = models.CharField(_("Account Holder Name"), max_length=255)
    account_no = models.IntegerField(_("Account Number"))
    bank_name = models.CharField(_("Bank Name"), max_length=255)
    ifsc_code = models.CharField(_("IFSC Code"), max_length=255)
    bank_branch = models.CharField(_("Bank Branch"), max_length=255)
    passbook = models.FileField(
        verbose_name=_("Passbook"),
        upload_to=staff_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.staff.first_name}"

    def __repr__(self):
        return f"<BankDetail(staff={self.staff})>"

    class Meta:
        verbose_name = 'Bank Detail'
        verbose_name_plural = 'Bank Details'


class SocialMedia(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Company'))
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_('Staff'))
    linkedin = models.URLField(_("LinkedIn Link"), blank=True, null=True)
    twitter = models.URLField(_(" Twitter Link"), blank=True, null=True)
    facebook = models.URLField(_("Facebook Link"), blank=True, null=True)
    instagram = models.URLField(_("Instagram Link"), blank=True, null=True)
    thread = models.URLField(_("Thread Link"), blank=True, null=True)
    github = models.URLField(_("Github Link"), blank=True, null=True)

    def __str__(self):
        return f"{self.staff.first_name}"

    def __repr__(self):
        return f"<SocialMedia(staff={self.staff})>"

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
