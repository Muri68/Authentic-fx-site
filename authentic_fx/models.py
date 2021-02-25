from django.db import models
from datetime import datetime, date


class Duration(models.Model):
    duration = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.duration


class Investor(models.Model):
    objects = None
    investor_name = models.CharField(max_length=30, blank=True)
    account_no = models.CharField(max_length=30, blank=True)
    bank_name = models.CharField(max_length=30, blank=True)
    amount_invested = models.CharField(max_length=30)
    date_of_investment = models.DateField("Date of Investment (mm/dd/yyyy)", auto_now_add=False, auto_now=False,
                                          blank=True, null=True)
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True)
    email_address = models.CharField(max_length=30)
    return_of_investment = models.CharField(max_length=30)
    due_date = models.DateField("Due Date (mm/dd/yyyy)", auto_now_add=False, auto_now=False, blank=True, null=True)
    users_name = models.CharField(max_length=30)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    complete = models.BooleanField(default=False)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.investor_name


class InvestorHistory(models.Model):
    objects = None
    investor_name = models.CharField(max_length=30, blank=True)
    account_no = models.CharField(max_length=30, blank=True)
    bank_name = models.CharField(max_length=30, blank=True)
    amount_invested = models.CharField(max_length=30)
    date_of_investment = models.DateField("Date of Investment (mm/dd/yyyy)", auto_now_add=False, auto_now=False,
                                          blank=True, null=True)
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True)
    email_address = models.CharField(max_length=30)
    return_of_investment = models.CharField(max_length=30)
    due_date = models.DateField("Due Date (mm/dd/yyyy)", auto_now_add=False, auto_now=False, blank=True, null=True)
    users_name = models.CharField(max_length=30)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.investor_name
