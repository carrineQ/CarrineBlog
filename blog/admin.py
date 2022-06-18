from django.contrib import admin
from blog.models import Banner, Category, Tag, Tui, Article, Link


@admin.register(Article)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    # 后台数据列表排序方式
    list_display_Links = ('id', 'title')
    # 设置哪些字段可以点击进入编辑界面


@admin.register(Banner)
class BlogBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(Category)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tui)
class BlogTuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Link)
class BlogLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')

# Register your models here.
