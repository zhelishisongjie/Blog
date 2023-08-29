from django.db import models
from django.contrib.auth.models import User
from article.models import Article


# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE , related_name="comments") # 级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = "created",

    def __str__(self):
        return self.body[:20]
