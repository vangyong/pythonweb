# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from system.models import User

from system import service


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


def user_list(request):
    context = {}
    context['hello'] = '用户列表'
    context['t_bool1'] = 'true'
    return render(request, 'system/user_list.html', context)


def user_add(request):
    userName = request.POST['userName']
    age = request.POST['age']
    email = request.POST['email']
    user = User()
    user.name = userName
    user.age = age
    user.email = email
    message = service.add_user(user)
    return HttpResponse(message)


def user_update(request):
    userName = request.POST['userName']
    age = request.POST['age']
    user = User()
    user.name = userName
    user.age = age
    message = service.update_user(user)
    return HttpResponse(message)
