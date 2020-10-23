from django.shortcuts import render

# Create your views here.
from crm import models


def index(request):
    return render(request, "sales/index.html")


def customer_list(request):
    print("客户库")
    return render(request, "customer/customers.html")
