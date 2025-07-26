from django.shortcuts import render
from django.http import HttpResponse


def students(request):
    return HttpResponse('<h2> Tomorrow is interview, Interview was good but make lots of mistake, I hope to get the job, ICC </h2>')
