# from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from Authentication.managers import UserManager
from Master.models import TimeStamp
from Master.myvalidator import mobile_validator
from General.models import Department, Designation, CompanyType
from imagekit.models import ProcessedImageField
from django.contrib.auth.hashers import make_password
from Master.uploader import company_directory_path, staff_directory_path
from django.db.models.signals import post_save
from django.dispatch import receiver
from io import BytesIO
from django.core.files import File
import qrcode
import uuid


class QRCodeMixin(models.Model):
    qr_code = models.ImageField(upload_to=staff_directory_path, blank=True, null=True)

    class Meta:
        abstract = True


class Company(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_code = models.CharField(_("Company Code"), max_length=6, unique=True)
    name = models.CharField(_('Company Name'), max_length=255, unique=True)
    company_type = models.ForeignKey(CompanyType, on_delete=models.SET_NULL, blank=True, null=True,
                                     verbose_name=_('Company Type'))
    registered_office_address = models.TextField(_('Registered Office Address'))
    company_logo = ProcessedImageField(upload_to=company_directory_path,
                                       options={'quality': 70}, blank=True, null=True)
    company_prefix = models.CharField(_("Company Prefix"), max_length=5, unique=True)

    def __str__(self):
        return f"{self.company_code} - {self.name}"

    def __repr__(self):
        return f"<Company(name={self.name})>"

    def save(self, *args, **kwargs):
        if not self.company_code:
            last_object = Company.objects.order_by('-id').first()
            if last_object and last_object.company_code:
                last_company_code = last_object.company_code
                company_code_suffix = last_company_code[-4:]
                new_suffix = str(int(company_code_suffix) + 1).zfill(4)
                self.company_code = f"{new_suffix}"
            else:
                self.company_code = "1001"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class User(AbstractUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Accountant', 'Accountant'),
        ('Manager', 'Manager'),
        ('HR', 'Human Resources'),
        ('Sales', 'Sales'),
        ('Employee', 'Employee'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(_('Role'), max_length=50, choices=ROLE_CHOICES, default='Employee')
    first_name = models.CharField(_('First Name'), max_length=255)
    middle_name = models.CharField(_('Middle Name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(_('Last Name'), max_length=255, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    phone = models.CharField(
        _("Mobile Number"),
        max_length=13,
        validators=[mobile_validator],
        help_text="Alphabets and special characters are not allowed (eg.+911234567890).",
    )
    gender = models.CharField(_('Gender'), max_length=50, choices=GENDER_CHOICES)
    dob = models.DateField(_('Date of Birth'), blank=True, null=True)

    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<User(email={self.email})>"

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Staff(QRCodeMixin, User):
    MARITAL_CHOICES = (
        ('Married', 'Married'),
        ('Single', 'Single'),
        ('Separated', 'Separated'),
        ('Widowed', 'Widowed'),
        ('Not Specified', 'Not Specified'),
    )
    BLOOD = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    CONTRACT_TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('other', 'Other'),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Company'))
    staff_id = models.CharField(_('Staff ID'), max_length=255, unique=True)
    alt_phone = models.CharField(
        _("Emergency Mobile Number"),
        max_length=13,
        validators=[mobile_validator],
        help_text="Alphabets and special characters are not allowed (eg.+911234567890).",
        blank=True, null=True
    )
    photo = ProcessedImageField(upload_to=staff_directory_path, options={'quality': 70}, blank=True, null=True)
    marital_status = models.CharField(_('Marital Status'), max_length=50, choices=MARITAL_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_('Department'))
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, verbose_name=_('Designation'))
    father_name = models.CharField(_('Father Name'), max_length=255, blank=True, null=True)
    mother_name = models.CharField(_('Mother Name'), max_length=255, blank=True, null=True)
    joining_date = models.DateField(_('Joining Date'), blank=True, null=True)
    contract_type = models.CharField(_('Contract Type'), max_length=50, choices=CONTRACT_TYPE_CHOICES)
    contract_start_date = models.DateField(_('Contract Start Date'), blank=True, null=True)
    contract_end_date = models.DateField(_('Contract End Date'), blank=True, null=True)
    experience = models.CharField(_('Experience'), max_length=50, blank=True, null=True)
    blood_group = models.CharField(_('Blood Group'), max_length=50, choices=BLOOD, blank=True, null=True)
    current_address = models.TextField(_('Current Address'))
    permanent_address = models.TextField(_('Permanent Address'))
    is_handicapped = models.BooleanField(_('Is Handicapped'), default=False)
    note = models.TextField(_('Note'), blank=True, null=True)

    def __str__(self):
        return self.staff_id

    def get_absolute_url(self):
        # current_site = Site.objects.get_current()
        # domain = current_site.domain
        return f'http://127.0.0.1:8000/employee/{self.staff_id}/'

    def __repr__(self):
        return f"<Staff(staff_id={self.staff_id})>"

    def save(self, *args, **kwargs):
        if not self.staff_id:
            # Generate staff_id based on company prefix and auto-increment
            last_staff = Staff.objects.filter(company=self.company).order_by('-id').first()
            if last_staff:
                last_staff_id = int(last_staff.staff_id[-1])
                new_staff_id = f"{self.company.company_prefix}{last_staff_id + 1:05d}"
            else:
                new_staff_id = f"{self.company.company_prefix}00001"
            self.staff_id = new_staff_id

        if self.pk is None or not Staff.objects.filter(pk=self.pk).exists():
            self.password = make_password(self.password)
        else:
            orig = Staff.objects.get(pk=self.pk)
            if orig.password != self.password:
                self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staffs')


@receiver(post_save, sender=Staff)
def generate_qr_code(sender, instance, created, **kwargs):
    if created and not instance.qr_code:
        data = instance.get_absolute_url()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        filename = f'qrcode_staff_{instance.staff_id}.png'
        instance.qr_code.save(filename, File(buffer), save=True)
