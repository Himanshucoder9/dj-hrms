from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from Authentication.models import Company, Staff
from Master.models import TimeStamp
from Master.myvalidator import mobile_validator, numeric, minimum, maximum, pan_validator
from imagekit.models import ProcessedImageField
from Master.uploader import staff_directory_path


class Education(models.Model):
    EDUCATION_CHOICES = (
        ('10th', '10th'),
        ('12th', '12th'),
        ('UG', 'Under Graduation'),
        ('PG', 'Post Graduation'),
        ('Other', 'Other'),
    )
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


class Document(models.Model):
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
        help_text="Upload document..", )

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
