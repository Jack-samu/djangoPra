from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
from random import choice, sample, randint

from blog.models import Post, Tag, Category
from comments.models import Comment


class Command(BaseCommand):
    help = '生成测试用数据'
    
    def handle(self, *args, **options):

        # 清理操作
        Post.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()
        Comment.objects.all().delete()
        User.objects.all().delete()

        categories = ['python学习', '工具', 'c&c++', '和父母打交道']
        tags = ['学习', '工具应用', '人生']

        for c in categories:
            Category.objects.create(name=c)
        for t in tags:
            Tag.objects.create(name=t)

        # 自定义子命令中的输出操作
        self.stdout.write(self.style.NOTICE("开始post。。。。。。"))
        
        fake = Faker('zh-CN')
        user = User.objects.create(username=fake.name(), password=fake.password())
        self.post_circle(fake, user)

        fake = Faker('en')
        user = User.objects.create(username=fake.name(), password=fake.password())
        self.post_circle(fake, user)
        self.stdout.write(self.style.SUCCESS("创建数据作业完成"))

    def post_circle(self, faker, user):
        for _ in range(10):
            # post部分信息
            title = faker.sentence(nb_words=8)
            content = faker.text(max_nb_chars=200)
            excerpt = content[:20]
            category = choice(Category.objects.all())
            tags = sample(list(Tag.objects.all()), randint(1, 3))

            post = Post.objects.create(
                title = title,
                content = content,
                excerpt = excerpt,
                category = category,
                author = user,
                created_time = faker.date_time_between(start_date='-1y', 
                                                    end_date='now', tzinfo=timezone.get_current_timezone())
            )
            Comment.objects.create(
                name = faker.name(),
                email = faker.email(),
                content = faker.paragraph(),
                post = post,
                created_time = faker.date_time_between(start_date='-1y', 
                                                      end_date='now', tzinfo=timezone.get_current_timezone())
            )
            post.tags.set(tags)