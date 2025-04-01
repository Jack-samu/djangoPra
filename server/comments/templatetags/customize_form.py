from django import template
from ..forms import CommentForm

register = template.Library()

@register.inclusion_tag("comment/_form.html")
def get_form(post, form=None):
    if form is None:
        form = CommentForm()
    return {'post':post, 'form':form}

from ..models import Comment

@register.inclusion_tag("comment/_list.html")
def show_comments(post):
    comments = Comment.objects.filter(post=post).order_by('-created_time')
    return {'comments':comments}