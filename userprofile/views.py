from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm


# Create your views here.


# 登录


def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data = request.POST)    # 表单
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data                 # 清洗出合法数据
            user = authenticate(username = data['username']  , password = data['password'])        # 如果均匹配则返回user对象
            if user:
                login(request , user)
                return redirect("article:article_list")         # 回到首页
            else:
                return HttpResponse("账号或密码输入错误，请重新输入") # 密码错误
        else:
            return HttpResponse("账号密码输入不合法")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {
            "form":user_login_form
        }
        return render( request , "userprofile/login.html" , context)
    else:
        return HttpResponse("请使用GET或者POST请求")


# 登出
def user_logout(request):
    logout(request)
    return redirect("article:article_list")


# 注册
def user_register(request):
    if request.method == "POST":
        user_register_form = UserRegisterForm(data = request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password( user_register_form.cleaned_data["password"] )        # def clean_这种写法Django会自动调用，验证密码
            new_user.save()
            login(request , new_user)
            return redirect("article:article_list")

        else:
            return HttpResponse("注册表单输入有误，请重新输入")
    elif request.method == "GET":
        user_register_form = UserRegisterForm()
        context = {
            "form" : user_register_form
        }
        return render(request , "userprofile/register.html" , context)
    else:
        return HttpResponse("请使用GET或者POST请求")
