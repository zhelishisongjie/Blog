from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# 文章模型
class Article(models.Model):
    id  = models.AutoField(primary_key = True)
    author = models.ForeignKey(User , on_delete=models.CASCADE)   # 级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    def get_absolute_rul(self):
        return reverse("article:article_detail" , args=[self.id] )