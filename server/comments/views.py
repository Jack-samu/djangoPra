from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from blog.models import Post
from .forms import CommentForm


@require_POST
def comment(req, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(req.POST)

    # 评论表单通过就保存
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(req, messages.SUCCESS, "评论发表", extra_tags='success')
        return redirect('blog:detail', title=post.title)
    messages.add_message(req, messages.ERROR, "评论发表失败，请检查", extra_tags='danger')
    return render(req, 'blog/detail.html', {'post':post, 'form':form, 'title':post.title})