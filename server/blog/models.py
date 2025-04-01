from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "栏目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}'

class Tag(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField("标题", max_length=60)
    excerpt = models.CharField("摘要", max_length=200, blank=True)
    content = models.TextField("正文")
    category = models.ForeignKey(Category, verbose_name="栏目", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name="标签", blank=True)
    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField()
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def view_increase(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return f'title: {self.title}, author: {self.author}, create:{self.created_time}'