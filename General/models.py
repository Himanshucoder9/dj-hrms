from django.db import models
from django.utils.translation import gettext_lazy as _
from Master.models import TimeStamp


class Role(TimeStamp):
    name = models.CharField(_('Role'), max_length=50, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Role(title={self.name})>"

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')


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
