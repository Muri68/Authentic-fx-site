from django.urls import path
from django.conf.urls import url
# from . views import InvestorDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('investor_entry/', views.investor_entry, name='investor_entry'),
    path('investors_list/', views.investors_list, name='investors_list'),
    path('investor_edit/<int:id>/', views.investor_edit, name='investor_edits'),
    path('investors_delete/<int:id>/', views.investor_delete, name='investor_delete'),
    url(r'^investorshistory_list/$', views.investorshistory_list, name='investorshistory_list'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^investor_detail/(?P<id>\d+)/$', views.investor_detail, name='investor_detail'),
    # path('investor_details/<int:pk>/', InvestorDetailView.as_view(), name='investor_details')

]
