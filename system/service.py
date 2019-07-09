# -*- coding: utf-8 -*-

from system.models import User
import uuid


def add_user(user):
    user.id = uuid.uuid1()
    user.save()
    return "success"


def update_user(user):
    # User.objects.filter(id=1).update(name='Google')
    return "success"


def list_user():
    # users = User.objects.all()
    users = None
    return users
