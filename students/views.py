from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    return HttpResponse('<h2> Last day my BOU Win 100$ in giveway </h2>')
