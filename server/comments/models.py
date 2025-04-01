from django.db import models
from django.utils import timezone

from blog.models import Post

# Create your models here.
class Comment(models.Model):
    name = models.CharField("名字", max_length=20)
    content = models.TextField("内容", max_length=300)
    email = models.EmailField("邮箱")
    created_time = models.DateTimeField(auto_now=timezone.now)
    post = models.ForeignKey(Post, verbose_name="相关联博客", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}, {self.content}"