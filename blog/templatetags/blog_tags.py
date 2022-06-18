# 通过{% load ... %}加载该标签或过滤器
# 要在模块内自定义标签，该模块必须包含一个名为register的模板层变量，
# 且他的值是template.Library的实例，所有的标签和过滤器都是在其中注册的
from django import template
register = template.Library()

@register.simple_tag(name='good')
def addstr_tag(strs):
    return 'Good morning'%strs