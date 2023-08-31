import markdown
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404,redirect

from comment.models import Comment
from .forms import ArticleForm

# Create your views here.

from .models import Article


# 文章列表
def article_list(request):
    search = request.GET.get("search")
    order = request.GET.get("order")

    if search:
        if order == "views":
            article_list = Article.objects.filter(
                Q(title__icontains=search) | Q(body__icontains=search)
            ).order_by("-views")
        else:
            article_list = Article.objects.filter(
                Q(title__icontains=search) | Q(body__icontains=search)
            )

    else :
        search = ""
        if order == "views":
            article_list = Article.objects.all().order_by("-views")
        else:
            article_list = Article.objects.all()


    # article_list = Article.objects.all() # 所有文章
    paginator = Paginator(article_list , 5)
    page = request.GET.get("page")
    articles = paginator.get_page(page)  # 每页的部分文章

    context = {
        "articles" : articles ,
        "order" : order,
        "search" : search
    }
    return render(request, "article/list.html" , context)




# 文章详情
# 函数中多了id这个参数。有了它才有办法知道到底应该取出哪篇文章
def article_details(request , id):
    article = Article.objects.get(id = id) # 在所有文章中，取出id值相符合的唯一的一篇文章
    article.views += 1                              # 浏览量+1
    article.save(update_fields=['views'])     # update_fields=[]指定了数据库只更新total_views字段，优化执行效率

    comments = Comment.objects.filter(article = id)
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])


    context = {
        "article" : article,
        "comments" : comments,
    }
    return render(request , "article/detail.html" , context)





# 在Article模型中， created和updated字段为自动生成，用户只需要填写title和body
# 新建文章
def article_create(request):
    if request.method == "POST":        # 用户提交数据
        article_post_form = ArticleForm(data = request.POST)        # 提交数据赋值到表单中
        if article_post_form.is_valid():                            # 判断数据是否满足模型要求
            new_article = article_post_form.save( commit= False)    # 保存数据，但不提交数据库（因为author还未指定）
            new_article.author = request.user                       # 作者为当前请求的用户名
            new_article.save()                                      # 新文章保存到数据库
            return redirect("article:article_list")                 # 完成后返回文章列表
        else:
            return HttpResponse("表单内容有错，请重新填写")

    else:       # (GET) 如果用户获取数据   ，  返回一个空的表单类对象，提供给用户填写
        article_post_form = ArticleForm()                           # 创建表单实例
        context = {                                                 # 赋值上下文
            "article_post_form":article_post_form
        }
        return render(request , "article/create.html"  , context)       # 返回模板




# 删除文章
def article_delete(request , id):
    # print(request.method)
    if request.method == "POST":
        article = Article.objects.get(id = id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许POST请求")


# 更新文章
def article_update(request , id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        article_post_form = ArticleForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail" , id=id)

        else:
            return HttpResponse("表单内容有误，请重新填写")

    else:
        article_post_form = ArticleForm()
        context = {
            "article":article,
            "article_post_form":article_post_form
        }
        return render( request , "article/update.html" , context)