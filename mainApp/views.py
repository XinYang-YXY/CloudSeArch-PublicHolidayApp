from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    context = {}
    context['name'] = 'yj'
    return render(request, 'index.html', context)