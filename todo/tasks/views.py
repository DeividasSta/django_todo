from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    return HttpResponse('hello from index')
