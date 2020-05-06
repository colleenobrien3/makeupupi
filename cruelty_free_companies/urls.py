from django.urls import path
from .views import CompanyList, redirect_view

urlpatterns = [
    path('companies', CompanyList.as_view(), name='company_list'),
    path('', redirect_view)
]
