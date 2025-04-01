from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from markdown import Markdown

from . import models

# Create your views here.
def index(req):
    post_list = models.Post.objects.all().order_by('-created_time')
    post_latest = post_list[:5]

    paginator = Paginator(post_list, 6)
    page = req.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render(req, 'blog/index.html', {'title':"Turtle'S Blog", 'post_list':posts, 'paginator': paginator, 'latests':post_latest})

def detail(req, title):
    # 使用django内置函数来进行post的条件查询，如果没有直接回404，挺方便的
    post = get_object_or_404(models.Post, title=title)
    md = Markdown(extensions=["markdown.extensions.extra",
                              "markdown.extensions.codehilite",
                              "markdown.extensions.toc"])
    # 数据库中markdown文本用md进行转换，得到html文本
    post.content = md.convert(post.content)
    # md解析后可以得到toc目录，直接赋值给post即可
    post.toc = md.toc
    return render(req, 'blog/detail.html', {'post':post, 'title':post.title})

def search(req):
    s = req.GET.get('s')

    if not s:
        messages.add_message(req, messages.ERROR, "关键词有点问题", extra_tags="danger")
        return redirect("blog:index")
    post_res = models.Post.objects.filter(Q(title__icontains=s) | Q(content__icontains=s))
    post_list = models.Post.objects.all().order_by('-created_time')[:5]
    messages.add_message(req, messages.SUCCESS, f'"{s}"的搜索结果如下：', extra_tags='success')
    return render(req, 'blog/index.html', {'title':"Turtle'S Blog", "post_list":post_res, 'latests':post_list})

def intro(req):
    return render(req, 'blog/introduction.html', {'title':'个人介绍'})

def archive(request):
    posts = models.Post.objects.all().order_by('-created_time')
    return render(request, 'blog/archive.html', {'posts': posts})