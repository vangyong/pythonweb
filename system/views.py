from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response

from system.models import User

from system import service


# Create your views here.

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
