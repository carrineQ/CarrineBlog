from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Article, Category, Banner, Tag, Link


def test_html(request):
    """视图方法中，render通过结合一个给定的模板和一个给定的字典，返回一个渲染后的HttpResponse对象"""
    return render(request, "blog/test.html", {'name': '百度'})


def test_url(request):
    return render(request, 'blog/test_url.html')


def father_html(request):
    return render(request, 'blog/father.html')


def son_html(request):
    name = 'xiaogou'
    course = ['11', '22', '33']
    return render(request, 'blog/son.html', locals())


def redict_url(request):
    return render(request, 'blog/new_test.html')


def test_to_reverse(request):
    return HttpResponseRedirect(
        reverse('blog:detail_hello',
                current_app=request.resolver_match.namespace))


def archive(request):
    articles = Article.objects.all()
    return render(request, 'blog/archive.html', {'articles': articles})


# def index(request):
#     articles = Article.objects.all()
#     return render(request, 'blog/index.html', {'articles': articles})


# 首页
def index(request):
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=4)[:3]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:10]
    link = Link.objects.all()
    return render(request, 'index.html', locals())


# 列表页
def list(request, lid):
    lists = Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)
    page = request.GET.get('page')
    paginator = Paginator(lists, 5)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    return render(request, 'list.html', locals())


# 内容页
def show(request, sid):
    shows = Article.objects.get(id=sid)
    hot = Article.objects.all().order_by('?')[:10]
    previous_blog = Article.objects.filter(created_time__gt=shows.created_time, category=shows.category.id).first()
    next_blog = Article.objects.filter(created_time__lt=shows.created_time, category=shows.category.id).last()
    shows.views = shows.views + 1
    shows.save()
    return render(request, 'show.html', locals())


# 标签页
def tag(request, tag):
    lists = Article.objects.filter(tags__name=tag)
    tname = Tag.objects.get(name=tag)
    page = request.GET.get('page')
    paginator = Paginator(lists, 5)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)

    return render(request, 'tags.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')
    lists = Article.objects.filter(title__icontains=ss)
    page = request.GET.get('page')
    paginator = Paginator(lists, 10)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    return render(request, 'search.html', locals())


# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())


def global_variable(request):
    allcategory = Category.objects.all()
    remen = Article.objects.filter(tui__id=2)[:6]
    tags = Tag.objects.all()
    return locals()
