from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from Master.models import TimeStamp
# Create your models here.

class CompanyType(TimeStamp):
    title = models.CharField(_('Company Type'),max_length=255, unique=True)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f"<CompanyType(title={self.title})>"
    
    class Meta:
        verbose_name = _('Company Type')
        verbose_name_plural = _('Company Types')


class Company(TimeStamp):
    company_code = models.CharField(_("Company Code"), max_length=6, unique=True)
    name = models.CharField(_('Company Name'), max_length=255, unique=True)
    company_type = models.ForeignKey(_('Company Type'), CompanyType, on_delete=models.SET_NULL, blank=True, null=True)
    registered_office_address = models.TextField(_('Registered Office Address'))
   
    def __str__(self):
        return f"{self.company_code} - {self.name}"
    
    def __repr__(self):
        return f"<CompanyType(title={self.title})>"
    
    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')