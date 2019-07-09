"""pythonweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import *
from . import view

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^hello$', view.hello),
    url(r'^search$', view.search),
    url(r'^search_get$', view.search_get),
    url(r'^search_post$', view.search_post),

    url(r'^user_list$', view.user_list),
    url(r'^user_add$', view.user_add),
    url(r'^user_update$', view.user_update),

]
