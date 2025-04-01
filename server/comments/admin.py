from django.contrib import admin

from . import models

class CommentAdmin(admin.ModelAdmin):
    # 评论模块的admin站点表单提交
    fields = ['name', 'content', 'post']
    list_display = ['name', 'email', 'created_time', 'post']

admin.site.register(models.Comment, CommentAdmin)