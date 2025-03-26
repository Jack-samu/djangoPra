from django.contrib import admin

from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    # post展示列表
    list_display = ['title', 'author', 'created_time', 'modified_time', 'category']
    # post进行提交的字段
    fields = ['title', 'excerpt', 'content', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


# admin站点工具中关联自定义model
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)