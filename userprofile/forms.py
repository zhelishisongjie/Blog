from django import forms
from django.contrib.auth.models import User


# 登录表单
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

# 注册表单
# 对数据库操作继承 ModelForm
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()
    password1 = forms.CharField()

    class Meta:
        model = User
        fields = ("username" , "email")

    # 两次密码一致检查
    def clean_password2(self): # 不能写clean_password ， 会导致password1中的数据被Django判定为无效数据从而清洗掉，从而password2属性不存在。最终导致两次密码输入始终会不一致，并且很难判断出错误原因
        data = self.cleaned_data
        if data.get("password") == data.get("password1"):
            return data.get("password")
        else :
            raise forms.ValidationError("两次密码输入不一致")