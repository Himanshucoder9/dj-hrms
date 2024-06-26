from django.db import models
from django.utils.translation import gettext_lazy as _
from Master.models import TimeStamp


# Create your models here.

class BreakType(TimeStamp):
    name = models.CharField(_("Name"), max_length=100)
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<BreakType(name={self.name})>"

    class Meta:
        verbose_name = _("Break Type")
        verbose_name_plural = _("Break Types")


class Break(models.Model):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    employee = models.ForeignKey('Authentication.Employee', on_delete=models.CASCADE, verbose_name=_("Employee"))
    start_time = models.TimeField(_("Start Time"))
    end_time = models.TimeField(_("End Time"))
    break_type = models.ForeignKey(BreakType, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name=_("Break Type"))

    def __str__(self):
        return self.break_type.name

    def __repr__(self):
        return f"<Break(break_type={self.break_type})>"

    class Meta:
        verbose_name = _("Break")
        verbose_name_plural = _("Breaks")


class Attendance(models.Model):
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('half_day', 'Half Day'),
        ('on_leave', 'On Leave'),
        ('holiday', 'Holiday'),
    )
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    employee = models.ForeignKey('Authentication.Employee', on_delete=models.CASCADE, verbose_name=_("Employee"))
    date = models.DateField(_("Date"))
    check_in = models.DateTimeField(null=True, blank=True, verbose_name=_("Check In"))
    check_out = models.DateTimeField(null=True, blank=True, verbose_name=_("Check Out"))
    breaks = models.ManyToManyField(Break, blank=True, null=True, verbose_name=_("Breaks"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name=_("Status"))
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
                                       verbose_name=_("Hours Worked"))

    def __str__(self):
        return self.status

    def __repr__(self):
        return f"<Attendance(employee={self.employee})>"

    class Meta:
        verbose_name = _("Attendance")
        verbose_name_plural = _("Attendances")


class LeaveType(TimeStamp):
    name = models.CharField(_("Name"), max_length=100)
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<LeaveType(name={self.name})>"

    class Meta:
        verbose_name = _("Leave Type")
        verbose_name_plural = _("Leave Types")


class LeaveRecord(TimeStamp):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    employee = models.ForeignKey('Authentication.Employee', on_delete=models.CASCADE, verbose_name=_("Employee"))
    leave_type = models.ForeignKey(LeaveType, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name=_("Leave Type"))
    from_date = models.DateField(_("From Date"))
    to_date = models.DateField(_("To Date"))
    reason = models.TextField(_("Reason"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name=_("Status"))
    reject_reason = models.TextField(_("Reject Reason"), blank=True, null=True)

    def __str__(self):
        return self.reason

    def __repr__(self):
        return f"<LeaveRecord(employee={self.employee})>"

    class Meta:
        verbose_name = _("Leave Record")
        verbose_name_plural = _("Leave Records")


class Holiday(TimeStamp):
    name = models.CharField(_("Name"), max_length=100)
    date = models.DateField(_("Date"))
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    description = models.TextField(_("Description"), blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Holiday(name={self.name})>"

    class Meta:
        verbose_name = _("Holiday")
        verbose_name_plural = _("Holidays")

