from django.db import models
from Master.models import TimeStamp
from django.utils.translation import gettext_lazy as _
import uuid


class IDCARD(TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    staff = models.ForeignKey('Authentication.Staff', on_delete=models.CASCADE, verbose_name=_("Staff"))
    issue_date = models.DateField(_("Issue Date"))

    def __str__(self):
        return f"{self.staff.staff_id} - {self.staff.first_name}"

    def __repr__(self):
        return f"<IDCARD(staff_id={self.staff.staff_id})>"

    class Meta:
        verbose_name = _('ID Card')
        verbose_name_plural = _('ID Cards')
