# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World 你好世界'
    context['t_bool1'] = 'true'
    return render(request, 'hello.html', context)
