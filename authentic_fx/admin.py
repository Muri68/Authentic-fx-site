from django.contrib import admin
from .models import Investor, Duration
from .forms import InvestorForm
from import_export.admin import ImportExportModelAdmin

# class InvestorAdmin(admin.ModelAdmin):
#     list_display = ["investor_name", "amount_invested", "date_of_investment", "duration", "return_of_investment", "due_date", "timestamp"]
#     form = InvestorForm
#     list_filter = ['investor_name', 'amount_invested', 'duration']
#     search_fields = ['investor_name', 'amount_invested', 'duration']

@admin.register(Investor, Duration)
class ViewAdmin(ImportExportModelAdmin):
	pass

# admin.site.register()
# admin.site.register()
