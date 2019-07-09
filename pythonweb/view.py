# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse




def hello(request):
    context = {}
    context['hello'] = 'Hello World 你好世界'
    context['t_bool1'] = 'true'
    return render(request, 'hello.html', context)


def search(request):
    return render(request, 'search.html')


# 接收请求数据
def search_get(request):
    ctx = {}
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
        ctx['res'] = message
    return render(request, "result.html", ctx)


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['res'] = request.POST['q']
    return render(request, "result.html", ctx)



