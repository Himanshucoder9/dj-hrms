from django.db import models
from django.utils.translation import gettext_lazy as _
from Master.models import TimeStamp


# Create your models here.
class PayrollPeriod(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"))
    is_locked = models.BooleanField(_("Is Locked"), default=False)

    def __str__(self):
        return f"{self.start_date} to {self.end_date}"

    def __repr__(self):
        return f"<PayrollPeriod(start_date={self.start_date}, end_date={self.end_date})>"

    class Meta:
        verbose_name = _("Payroll Period")
        verbose_name_plural = _("Payroll Periods")


class PayrollEntry(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    staff = models.ForeignKey('Authentication.Staff', on_delete=models.SET_NULL, null=True, verbose_name=_("Staff"))
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE, verbose_name=_("Payroll Period"))
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Basic Salary"))
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Allowances"))
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Deductions"))
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Net Salary"))
    # Additional fields for more detailed breakdown
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name=_("Overtime Hours"))
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Bonus"))
    penalties = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Penalties"))
    other_allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           verbose_name=_("Other Allowances"))

    def calculate_net_salary(self):
        self.net_salary = self.basic_salary + self.allowances - self.deductions + self.overtime_hours - self.penalties + self.bonus + self.other_allowances
        self.save()

    def __str__(self):
        return f"Payroll for {self.staff} - {self.payroll_period}"

    def __repr__(self):
        return f"<PayrollEntry(staff={self.staff}, payroll_period={self.payroll_period})>"

    class Meta:
        verbose_name = _("Payroll Entry")
        verbose_name_plural = _("Payroll Entries")


class PayrollAdjustment(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    staff = models.ForeignKey('Authentication.Staff', on_delete=models.CASCADE, verbose_name=_("Staff"))
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE, verbose_name=_("Payroll Period"))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    reason = models.TextField(_("Reason"))

    def __str__(self):
        return f"Adjustment for {self.staff} - {self.payroll_period}"

    def __repr__(self):
        return f"<PayrollAdjustment(staff={self.staff}, payroll_period={self.payroll_period})>"

    class Meta:
        verbose_name = _("Payroll Adjustment")
        verbose_name_plural = _("Payroll Adjustments")


class PayrollReport(TimeStamp):
    payroll_period = models.OneToOneField(PayrollPeriod, on_delete=models.CASCADE, verbose_name=_("Payroll Period"),
                                          primary_key=True)
    total_salary_paid = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("Total Salary Paid"))
    total_allowances_paid = models.DecimalField(max_digits=15, decimal_places=2,
                                                verbose_name=_("Total Allowances Paid"))
    total_deductions = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("Total Deductions"))
    total_net_amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("Total Net Amount"))

    def generate_report(self):
        # Example method to calculate totals based on PayrollEntries
        entries = PayrollEntry.objects.filter(payroll_period=self.payroll_period)
        self.total_salary_paid = entries.aggregate(Sum('basic_salary'))['basic_salary__sum'] or Decimal('0.00')
        self.total_allowances_paid = entries.aggregate(Sum('allowances'))['allowances__sum'] or Decimal('0.00')
        self.total_deductions = entries.aggregate(Sum('deductions'))['deductions__sum'] or Decimal('0.00')
        self.total_net_amount = entries.aggregate(Sum('net_salary'))['net_salary__sum'] or Decimal('0.00')
        self.save()

    def __str__(self):
        return f"Payroll Report for {self.payroll_period}"

    def __repr__(self):
        return f"<PayrollReport(payroll_period={self.payroll_period})>"

    class Meta:
        verbose_name = _("Payroll Report")
        verbose_name_plural = _("Payroll Reports")
