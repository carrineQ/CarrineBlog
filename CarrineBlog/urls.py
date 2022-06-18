"""CarrineBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
# 主路由，path()中的第一个引号为templates的下一级，然后交由include里的二级路由去调用其视图方法

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls','blog'),namespace='first')),

    path('ueditor/', include('DjangoUeditor.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    path('', views.index, name='index'),
    path('list-<int:lid>.html', views.list, name='list'),
    path('show-<int:sid>.html', views.show, name='show'),
    path('tag/<tag>', views.tag, name='tags'),
    path('s/', views.search, name='search'),
    path('about/', views.about, name='about'),

]
