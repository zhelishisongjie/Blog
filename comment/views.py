from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse

from article.models import Article
from .forms import CommentForm

# Create your views here.

# 评论
@login_required(login_url="/login")  # 需要先登录
def post_comment(request , article_id):
    article = get_object_or_404(Article , id = article_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save( commit = False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            detail_url=reverse('article:article_detail', args=[article_id])
            return redirect(detail_url)

        else:
            return HttpResponse("表单内容有误，请重新填写")
    else :
        return HttpResponse("发表评论仅接受POST请求")