from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from Authentication.managers import UserManager
from Master.models import TimeStamp
from Master.myvalidator import mobile_validator, numeric, minimum, maximum, pan_validator
from General.models import Department, Designation
from imagekit.models import ProcessedImageField
from django.contrib.auth.hashers import check_password, make_password
from Master.uploader import company_directory_path, expense_directory_path, employee_directory_path


class CompanyType(TimeStamp):
    name = models.CharField(_('Company Type'), max_length=255, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<CompanyType(title={self.name})>"

    class Meta:
        verbose_name = _('Company Type')
        verbose_name_plural = _('Company Types')


class Company(TimeStamp):
    company_code = models.CharField(_("Company Code"), max_length=6, unique=True)
    name = models.CharField(_('Company Name'), max_length=255, unique=True)
    company_type = models.ForeignKey(CompanyType, on_delete=models.SET_NULL, blank=True, null=True,
                                     verbose_name=_('Company Type'))
    registered_office_address = models.TextField(_('Registered Office Address'))
    company_logo = ProcessedImageField(upload_to=company_directory_path,
                                       options={'quality': 70}, blank=True, null=True)

    def __str__(self):
        return f"{self.company_code} - {self.name}"

    def __repr__(self):
        return f"<Company(name={self.name})>"

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


class Employee(User):
    MARITAL_CHOICES = (
        ('Married', 'Married'),
        ('Single', 'Single'),
        ('Separated', 'Separated'),
        ('Widowed', 'Widowed'),
        ('Not Specified', 'Not Specified'),
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
    photo = ProcessedImageField(upload_to=employee_directory_path, options={'quality': 70}, blank=True, null=True)
    marital_status = models.CharField(_('Marital Status'), max_length=50, choices=MARITAL_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_('Department'))
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, verbose_name=_('Designation'))
    father_name = models.CharField(_('Father Name'), max_length=255, blank=True, null=True)
    mother_name = models.CharField(_('Mother Name'), max_length=255, blank=True, null=True)
    joining_date = models.DateField(_('Joining Date'), blank=True, null=True)
    contact = models.CharField(_('Contact'), max_length=255, blank=True, null=True)
    current_address = models.TextField(_('Current Address'))
    permanent_address = models.TextField(_('Permanent Address'))

    def __str__(self):
        return self.staff_id

    def __repr__(self):
        return f"<Employee(staff_id={self.staff_id})>"

    def save(self, *args, **kwargs):
        if self.pk is None or not Employee.objects.filter(pk=self.pk).exists():
            self.password = make_password(self.password)
        else:
            orig = Employee.objects.get(pk=self.pk)
            if orig.password != self.password:
                self.password = make_password(self.password)
        super().save(*args, **kwargs)
    @classmethod
    def authenticate(cls, company_code, staff_id, password):
        try:
            employee = cls.objects.get(company__company_code=company_code, staff_id=staff_id)
            if check_password(password, employee.password):
                return employee
        except cls.DoesNotExist:
            return None

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')


class Education(models.Model):
    EDUCATION_CHOICES = (
        ('10th', '10th'),
        ('12th', '12th'),
        ('UG', 'Under Graduation'),
        ('PG', 'Post Graduation'),
        ('Other', 'Other'),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('Company'))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
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
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
    aadhar_no = models.CharField(_("Aadhar Number"), max_length=12, null=True,
                                 validators=[numeric("Aadhar Number"), minimum(12, 'Aadhar '
                                                                                   'number'),
                                             maximum(12, 'Aadhar number')],
                                 help_text="Only numbers are allowed.")
    pan_no = models.CharField(_("Pan Number"), max_length=10, validators=[pan_validator])
    aadhar_document = models.FileField(
        verbose_name=_("Aadhar Document"),
        upload_to=expense_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'webp'])],
        help_text="Upload document..", )

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
