from django.db import models
from django.utils.translation import gettext_lazy as _
from Master.models import TimeStamp


class CompanyType(TimeStamp):
    name = models.CharField(_('Company Type'), max_length=255, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<CompanyType(title={self.name})>"

    class Meta:
        verbose_name = _('Company Type')
        verbose_name_plural = _('Company Types')


class Designation(TimeStamp):
    name = models.CharField(_('Designation'), max_length=50, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Designation(title={self.name})>"

    class Meta:
        verbose_name = _('Designation')
        verbose_name_plural = _('Designations')


class Department(TimeStamp):
    name = models.CharField(_('Department'), max_length=50, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Department(title={self.name})>"

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
