from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import csv
from django.contrib import messages
from datetime import date
# from django.views.generic import


# Create your views here.

def home(request):
    title = 'Authentic Global Market'
    context = {
        "title": title,
    }
    return render(request, "base.html", context)


def investor_entry(request):
    title = "Add Investor"
    form = InvestorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Investor Successfully Saved')
        return redirect('/investors_list')
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "investor_entry.html", context)


def investors_list(request):
    title = "List of all Investors"
    queryset = Investor.objects.all().order_by('complete','due_date')
    form = InvestorSearchForm(request.POST or None)
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Investor.objects.all().order_by('timestamp').filter(
            investor_name__icontains=form['investor_name'].value(), account_no__icontains=form['account_no'].value())
        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }

        if form['export_to_CSV'].value():
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Investors list.csv"'
            writer = csv.writer(response)
            writer.writerow(
                {'INVESTOR NAME', 'ACCOUNT NO', 'BANK NAME', 'AMOUNT INVESTED', 'DATE OF INVESTMENT', 'DURATION',
                 'PHONE NUMBER', 'EMAIL ADDRESS', 'RETURN OF INVESTMENT', 'DUE DATE', 'ADDED BY', 'DATE CREATED'})
            instance = queryset
            for row in instance:
                writer.writerow(
                    [row.investor_name, row.account_no, row.bank_name, row.amount_invested, row.date_of_investment,
                     row.duration, row.phone_number, row.email_address, row.return_of_investment, row.due_date,
                     row.users_name, row.timestamp])
            return response

    return render(request, "investors_list.html", context)


# EDIT VIEW
def investor_edit(request, id=None):
    instance = get_object_or_404(Investor, id=id)
    form = InvestorForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, str(instance.investor_name) + '  ' + 'Edited Successfully')
        return redirect('/investors_list')

    context = {
        "title": 'Edit ' + str(instance.investor_name),
        "instance": instance,
        "form": form,
    }
    return render(request, "investor_entry.html", context)


# Detail PAGE
def investor_detail(request, id=None):
    # instance = Investor.objects.get(id=id)
    instance = get_object_or_404(Investor, id=id)

    context = {
        "title": 'Full Details of ' + str(instance.investor_name),
        "instance": instance,
    }
    return render(request, "investor_detail.html", context)




def investor_delete(request, id=None):
    instance = get_object_or_404(Investor, id=id)
    if request.method == 'POST':
        instance.delete()
        messages.success(request, 'Investor Deleted Successfully')
        return redirect('/investors_list')
    context = {
        'instance':instance
    }
    return render(request, 'delete_investor.html', context)


# To SHOW UPDATE
def investorshistory_list(request):
    title = 'Update History'
    queryset = InvestorHistory.objects.all().order_by('-timestamp')
    context = {
       "title": title,
       "queryset": queryset,
    }
    return render(request, "investorshistory_list.html",context)



def settings(request):
    title = 'Add Investment Duration'
    form = DurationSystemForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/investors_list')
    context = {
        "title": title,
        "form": form,
        }
    return render(request, "settings.html",context)
