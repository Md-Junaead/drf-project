from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    return HttpResponse('<h2> Hello Traders, today loss 600 taka </h2>')
