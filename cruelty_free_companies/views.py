from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CompanySerializer
from .models import Company
from django.shortcuts import redirect


class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


def redirect_view(request):
    response = redirect('/companies')
    return response
