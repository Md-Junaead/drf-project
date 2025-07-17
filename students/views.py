from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    return HttpResponse('<h2> 175 taka for referral </h2>')
