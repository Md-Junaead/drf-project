from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    return HttpResponse('<h2> I am not gonna stop untill i success </h2>')
