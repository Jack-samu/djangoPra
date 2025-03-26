from django.shortcuts import render, get_object_or_404

from . import models

# Create your views here.
def index(req):
    post_list = models.Post.objects.all()
    return render(req, 'blog/index.html', {'title':"Turtle'S Blog", 'post_list':post_list})

def detail(req, title):
    # 使用django内置函数来进行post的条件查询，如果没有直接回404，挺方便的
    post = get_object_or_404(models.Post, title=title)
    return render(req, 'blog/detail.html', {'post':post})