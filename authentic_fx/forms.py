from django import forms
from .models import Investor, Duration


class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ['investor_name', 'account_no', 'bank_name', 'amount_invested', 'date_of_investment', 'duration',
                  'phone_number', 'email_address', 'return_of_investment', 'due_date', 'users_name', 'complete']


class InvestorSearchForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = ['investor_name', 'account_no']


class DurationSystemForm(forms.ModelForm):
    class Meta:
        model = Duration
        fields = ['duration']