from django.shortcuts import render
from django.http import HttpResponse


def my_blog(request):
    return HttpResponse("Hello, blog!")
