from django.urls import path
from . import views
app_name = 'blog'
# 二级路由，path()的第一个分号为在URL中的名字，通过views.方法打开静态网页
urlpatterns = [
    # 这里的name可以作为html网页内的url连接名称，做到页面跳转的作用
    path('test',views.test_html,name='test'),
    path('Hello_Web/',views.test_url,name='hello'),
    path('father/',views.father_html),
    path('son/',views.son_html),
    path('test_url/',views.test_html,name='detail_hello'),
    path('redict/',views.redict_url),
    path('reverse/',views.test_to_reverse),
    path('archive/',views.archive),
    path('', views.index),

]