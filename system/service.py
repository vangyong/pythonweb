# -*- coding: utf-8 -*-

from system.models import User


def add_user(user):
    user = User.objects
    user.name = 'Google'
    user.save()
    return "success"


def update_user(user):
    User.objects.filter(id=1).update(name='Google')
    return "success"


def list_user():
    return User.objects.all()
