from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from Master.models import TimeStamp
from decimal import Decimal


class StaffBasicPayroll(TimeStamp):
    company = models.ForeignKey('Authentication.Company', on_delete=models.CASCADE, verbose_name=_("Company"))
    staff = models.ForeignKey('Authentication.Staff', on_delete=models.CASCADE, verbose_name=_("Staff"))
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Basic Salary"))
    hra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("House Rent Allowance (HRA)"))
    conveyance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Conveyance Allowance"))
    medical_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Medical Allowance"))
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Special Allowance"))
    epf_number = models.CharField(max_length=20, verbose_name=_("EPF Number"), blank=True, null=True)
    esi_number = models.CharField(max_length=20, verbose_name=_("ESI Number"), blank=True, null=True)
    professional_tax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Professional Tax"),
                                           default=0)
    tds = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Tax Deducted at Source (TDS)"),
                              default=0)

    def __str__(self):
        return f"Payroll details for {self.staff}"

    def __repr__(self):
        return f"<StaffBasicPayroll(staff={self.staff}, company={self.company})>"

    class Meta:
        verbose_name = _("Staff Basic Payroll")
        verbose_name_plural = _("Staff Basic Payrolls")


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
    staff = models.ForeignKey('Authentication.Staff', on_delete=models.CASCADE, verbose_name=_("Staff"))
    payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE, verbose_name=_("Payroll Period"))
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Basic Salary"))
    hra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("House Rent Allowance (HRA)"), default=0)
    conveyance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Conveyance Allowance"), default=0)
    medical_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Medical Allowance"),
                                            default=0)
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Special Allowance"),
                                            default=0)
    epf_contribution = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("EPF Contribution"),
                                           default=0)
    esi_contribution = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("ESI Contribution"),
                                           default=0)
    professional_tax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Professional Tax"),
                                           default=0)
    tds = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Tax Deducted at Source (TDS)"),
                              default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Net Salary"), editable=False)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name=_("Overtime Hours"))
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Bonus"))
    penalties = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Penalties"))
    other_allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           verbose_name=_("Other Allowances"))

    def calculate_net_salary(self):
        self.net_salary = (
                self.basic_salary +
                self.hra +
                self.conveyance +
                self.medical_allowance +
                self.special_allowance +
                self.other_allowances -
                self.epf_contribution -
                self.esi_contribution -
                self.professional_tax -
                self.tds +
                self.bonus -
                self.penalties +
                (self.overtime_hours * self.get_overtime_rate())
        )
        self.save()

    def get_overtime_rate(self):
        return Decimal('1.5') * (self.basic_salary / Decimal('160'))

    def save(self, *args, **kwargs):
        self.calculate_net_salary()
        super().save(*args, **kwargs)

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
    total_basic_salary = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("Total Basic Salary"),
                                             default=0)
    total_hra = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("Total HRA"), default=0)
    total_conveyance = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("Total Conveyance"),
                                           default=0)
    total_medical_allowance = models.DecimalField(max_digits=15, decimal_places=2,
                                                  verbose_name=_("Total Medical Allowance"), default=0)
    total_special_allowance = models.DecimalField(max_digits=15, decimal_places=2,
                                                  verbose_name=_("Total Special Allowance"), default=0)
    total_epf_contribution = models.DecimalField(max_digits=15, decimal_places=2,
                                                 verbose_name=_("Total EPF Contribution"), default=0)
    total_esi_contribution = models.DecimalField(max_digits=15, decimal_places=2,
                                                 verbose_name=_("Total ESI Contribution"), default=0)
    total_professional_tax = models.DecimalField(max_digits=15, decimal_places=2,
                                                 verbose_name=_("Total Professional Tax"), default=0)
    total_tds = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("Total TDS"), default=0)
    total_net_salary = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("Total Net Salary"),
                                           default=0)

    def generate_report(self):
        entries = PayrollEntry.objects.filter(payroll_period=self.payroll_period)
        self.total_basic_salary = entries.aggregate(Sum('basic_salary'))['basic_salary__sum'] or Decimal('0.00')
        self.total_hra = entries.aggregate(Sum('hra'))['hra__sum'] or Decimal('0.00')
        self.total_conveyance = entries.aggregate(Sum('conveyance'))['conveyance__sum'] or Decimal('0.00')
        self.total_medical_allowance = entries.aggregate(Sum('medical_allowance'))['medical_allowance__sum'] or Decimal(
            '0.00')
        self.total_special_allowance = entries.aggregate(Sum('special_allowance'))['special_allowance__sum'] or Decimal(
            '0.00')
        self.total_epf_contribution = entries.aggregate(Sum('epf_contribution'))['epf_contribution__sum'] or Decimal(
            '0.00')
        self.total_esi_contribution = entries.aggregate(Sum('esi_contribution'))['esi_contribution__sum'] or Decimal(
            '0.00')
        self.total_professional_tax = entries.aggregate(Sum('professional_tax'))['professional_tax__sum'] or Decimal(
            '0.00')
        self.total_tds = entries.aggregate(Sum('tds'))['tds__sum'] or Decimal('0.00')
        self.total_net_salary = entries.aggregate(Sum('net_salary'))['net_salary__sum'] or Decimal('0.00')
        self.save()

    def __str__(self):
        return f"Payroll Report for {self.payroll_period}"

    def __repr__(self):
        return f"<PayrollReport(payroll_period={self.payroll_period})>"

    class Meta:
        verbose_name = _("Payroll Report")
        verbose_name_plural = _("Payroll Reports")
