from django.db import models
from django.utils.translation import gettext_lazy as _
from Master.models import TimeStamp


class Role(TimeStamp):
    title = models.CharField(_('Role'), max_length=50, unique=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Role(title={self.title})>"

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
    
    
    